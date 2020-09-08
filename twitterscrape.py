import tweepy
from tweepy import OAuthHandler
import json
import wget
import time
import sqlite3
import database
import os.path

consumer_key = 'yevA9LdQA5XNL1VQ13rWgFZnz'
consumer_secret = 'If9W4cO7dFI1NOwrVGogdFdok60SP2edVY14aH7YCWK9VYhRtL'
access_token = '173834439-1KzhkEo69bzHAW3BLH2vv7xXHZFO7enV5MAJzHKu'
access_secret = 'Hx0fQCmjXI19RTZwdASY6g62IFATeqkzyGnSmg05Y7Yat'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Setup Database Connections
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "testDatabase.db")
print(db_path)
conn = database.create_connection(db_path)

displayName = 'SakataniYen'

tweets = api.user_timeline(screen_name= displayName,
                           count=200, include_rts=False,
                           exclude_replies=True)
last_id = tweets[-1].id

x=0
while (x<5):
     more_tweets = api.user_timeline(screen_name= displayName,count=200,include_rts=False,exclude_replies=True,max_id=last_id-1)
     time.sleep(1)
     x=x+1
     if (len(more_tweets) == 0):
         print ("nothing")
     else:
      last_id = more_tweets[-1].id-1
      tweets = tweets + more_tweets
     ## print(more_tweets)

media_files = set()
print("the number of tweets went through was ", len(tweets))
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
      #  print(media[0]['media_url'])
        picture = (media[0]['media_url'],displayName)
        image_id = database.create_image(conn,picture)
        print(image_id)
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)

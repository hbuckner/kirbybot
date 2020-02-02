import twilio
import twilio.rest
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
         body='This is a test?',
         from_='+14253744306',
         media_url=['https://raw.githubusercontent.com/hbuckner/kirbybot/master/EFuK41IU8AE7xV9.jpg'],
         to='+18435999080'
     )

print(message.sid)

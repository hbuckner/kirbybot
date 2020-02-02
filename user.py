
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password = "megaman1", host ="127.0.0.1", port="5432")
cur = con.cursor()
print("database opened succesfully")

class User:
    def __init__(self,phone,imageId,sentToday):
        self.phone = phone
        self.imageId = imageId
        self.sentToday = sentToday


#Creates a user
def createUser(phone,imageID,sentToday):
    newUser = User(phone,imageID,sentToday)
    cur.execute("INSERT into tbl_user (PHONE,IMAGEID,SENTTODAY) values(%s,%s,%s)", (phone,imageID,sentToday))
    con.commit()
    print("Record inserted successfully")

#Deletes a user
def deleteUser(phone):
    cur.execute('DELETE from tbl_user WHERE phone = %s',(phone,))
    con.commit()
    print("Record deleted successfully")

#Updates the UserImageID
def updateUserImageId(phone,imageID):
    cur.execute('UPDATE tbl_user set imageID = %s where phone =%s', (imageID,phone))
    con.commit()
    print("Record updated successfully")
    return self

def updateUserSentToday(phone,sentToday):
    cur.execute('UPDATE tbl_user set sentToday = %s where phone =%s', (sentToday,phone))
    con.commit()
    print("Record updated successfully")
    return self


#deleteUser
#createUser(12343556,12,True)
# phonenumb='12343556'
# deleteUser(phonenumb)
updateUserImageId('12343556','12345678')
updateUserSentToday('12343556','False')

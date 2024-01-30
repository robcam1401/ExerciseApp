from Insert import *
import datetime

########################
# Unit tests for inserting, deleting, and modifying data in the UserAccount database




# connects to the sql server and queries for all account numbers in the UserAccount table
def ConnectAndQuery():
    cnx,cursor = connect()

    query1=("SELECT AccountNumber FROM UserAccount")
    query2=("SELECT VideoLink FROM Videos WHERE VideoID = 1")
    query3=("SELECT * FROM Friends")
    cursor.execute(query3)

    for item in cursor:
        print(item)

    cursor.close()
    cnx.close()
    return

# connects to the sql server and inserts into the UserAccount table
def ConnectAndInsert():

    data_user = {
        "AccountNumber" : 1,
        "Username" : "Admin",
        "Email" : "user@user.com",
        "PhoneNumber" : 1,
        "Fname" : "Zach",
        "Minit" : "W",
        "Lname" : "Nalepa",
        "UserDoB" : datetime.date(2001,7,20)
    }
    data_user1 = {
        "AccountNumber" : 2,
        "Username" : "GenericUser",
        "Email" : "user2@user.com",
        "PhoneNumber" : 1111111111,
        "Fname" : "Generic",
        "Minit" : "A",
        "Lname" : "User",
        "UserDoB" : datetime.date(2000,1,1)
    }

    data_Video = {
        "VideoID" : None,
        "AccountNumber" : 1,
        "Video Title" : "First Video",
        "VidDescription" : "The first video uploaded to our app",
        "Category" : "dev"
    }

    data_friends = {
        "User1ID" : 1,
        "User2ID" : 2,
        "PairID" : 1
    }

    #newAccountInsert(data_user1)
    newFriendsInsert(data_friends)
    #Insert.newVideoInsert(data_Video, VideoLink, Thumbnail)
    return

ConnectAndInsert()
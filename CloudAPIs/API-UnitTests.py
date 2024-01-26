import Insert
import datetime

########################
# Unit tests for inserting, deleting, and modifying data in the UserAccount database




# connects to the sql server and queries for all account numbers in the UserAccount table
def ConnectAndQuery():
    cnx,cursor = Insert.connect()

    query=("SELECT AccountNumber FROM UserAccount")
    cursor.execute(query)

    for (number) in cursor:
        print(number)

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
        "UserDoB" : (2001,7,20)
    }

    data_Video = {
        "VideoID" : None,
        "AccountNumber" : 1,
        "Video Title" : "First Video",
        "VidDescription" : "The first video uploaded to our app",
        "Category" : "dev"
    }

    Insert.newAccountInsert(data_user)
    #Insert.newVideoInsert(data_Video, VideoLink, Thumbnail)
    return

ConnectAndQuery()
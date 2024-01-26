import mysql.connector
import datetime

#######################################################
# This insert file and the other modify and delete file
# are intended to run on an authenticator server instead of a user device
# The users will send their information to the server, which will interface
# with the sql server in theri place. For now, this file will
# run on the test devices and will eventually move to the server.
#######################################################
# This file uses the mysql connector library v9 for python 3.12, to install:
# pip install mysql-connector-python 


## Helper Methods mainly type-checking

def connect():
    cnx = mysql.connector.connect(user='GenericUser',host='34.121.87.64',database='ExerciseApp')
    cursor = cnx.cursor()
    return cnx,cursor

def getLastID(table : str, identifier):
    cnx, cursor = connect()
    # the table is selected by the calling function
    # this way this function is generic for all tables
    last_row = ('SELECT {}\
                FROM {}\
                ORDER BY {} DESC LIMIT 1').format(identifier,table,identifier)
    cursor.execute(last_row)

    cursor.close()
    cnx.close()

    return int(cursor.__str__())

## Type Checking

# when inserting, columns will be strongly-typed at insert and will be checked to see if they are within the declared parameters
# for example, username is strongly typed as a string and will be checked to see if it is 15 characters or less
def newAccountTypeCheck(AccInfo):
    if len(AccInfo['Username']) > 15:
        raise "Username too long"
    if len(AccInfo['Email']) > 32:
        raise "Email too long"
    if AccInfo['PhoneNumber'] > 99999999999:
        raise "Phone number too large"
    if len(AccInfo['Fname']) > 15:
        raise "First name too long"
    if len(AccInfo['Minit']) > 1:
        raise "Middle Initial too long"
    if len(AccInfo['Lname']) > 15:
        raise "Last name too long"
    try: 
        AccInfo['UserDoB'] = datetime.date(AccInfo['UserDoB'])
    except:
        raise "Invalid Date of Birth"
    return

## Insert Methods

# Insert a new Account with given account information in a dictionary
def newAccountInsert(AccInfo):
    # check for valid data
    newAccountTypeCheck(AccInfo)

    cnx,cursor = connect()
    AccInfo['AccountNumber'] = getLastID('UserAccount','AccountNumber') + 1
    add_User = ("INSERT INTO UserAccount "
              "(AccountNumber, Username, Email, PhoneNumber,Fname,Minit,Lname,UserDoB)"
              "VALUES (%(AccountNumber)s, %(Username)s, %(Email)s, %(PhoneNumber)s, %(Fname)s, %(Minit)s, %(Lname)s, %(UserDoB)s)")
    cursor.execute(add_User,AccInfo)
    cnx.commit()


    cursor.close()
    cnx.close()
    return

# Insert a new video with given video information and a video and thumbnail file
def newVideoInsert(VideoInfo, VideoLink, Thumbnail):

    cnx,cursor = connect()
    VideoInfo['VideoID'] = getLastID('Videos','VideoID') + 1
    # VideoLink, Views, Thumbnail, Upload Date will be auto-completed with a trigger when the row is inserted
    add_Video = ("INSERT INTO UserAccount "
              "(VideoID, AccountNumber, VideoTitle,VidDescription,Category,Thumbnail)"
              "VALUES (%(VideoID)s, %(AccountNumber)s, %(VideoTitle)s, %(VidDescription)s, %(Category)s, %(Thumbnail)s)")

    cursor.execute(add_Video, VideoInfo)
    cnx.commit()

    cursor.close()
    cnx.close()
    return

def newCommentInsertVideo(CommentInfo):
    cnx,cursor = connect()
    CommentInfo['CommentID'] = getLastID('Comments','CommentID') + 1
    add_comment = ("INSERT INTO Comments "
              "(CommentID, AccountNumber, CommentBody, VideoComment,ThreadParent)"
              "VALUES (%(CommentID)s, %(AccountNumber)s, %(CommentBody)s, %(VideoComment)s, %(ThreadParent)s)")
    
    cursor.execute(add_comment,CommentInfo)
    cnx.commit()

    cursor.close()
    cnx.close()
    return
def newCommentInsertContent(CommentInfo):
    cnx,cursor = connect()
    CommentInfo['CommentID'] = getLastID('Comments','CommentID') + 1
    add_comment = ("INSERT INTO Comments "
              "(CommentID, AccountNumber, CommentBody, ContentComment,ThreadParent)"
              "VALUES (%(CommentID)s, %(AccountNumber)s, %(CommentBody)s, %(ContentComment)s, %(ThreadParent)s)")

    cursor.execute(add_comment,CommentInfo)
    cnx.commit()

    cursor.close()
    cnx.close()
    return

def newContentInsert(ContentInfo):
    cnx,cursor = connect()
    ContentInfo['ContentID'] = getLastID('Content','ContentID') + 1
    add_content = ("INSERT INTO Content "
              "(ContentID, Category, AccountNumber, BodyDescription,ContentLink)"
              "VALUES (%(ContentID)s, %(Category)s, %(BodyDescription)s, %(ContentLink)s, %(ThreadParent)s)")


    cursor.close()
    cnx.close()
    pass

def newContentInsert(ContentInfo,Link):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newFriendsInsert(FriendInfo):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newFriendMessages(MessageInfo):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newFriendMessages(MessageInfo,Link):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newCommunityInsert(CommInfo):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newCommMessages(MessageInfo):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newCommMessages(MessageInfo,Link):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass

def newEvent(EventInfo):
    cnx,cursor = connect()


    cursor.close()
    cnx.close()
    pass
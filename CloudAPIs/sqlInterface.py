# required imports
import sys
import os

# find absolute paths
_CloudAPIs =  os.path.join(os.getcwd(), os.path.dirname("CloudAPIs"))
_libs =  os.path.join(os.getcwd(), os.path.dirname("libs"))

# insert into path variables
sys.path.insert(0,_CloudAPIs)
sys.path.insert(0,_libs)

# import from path variables
from CloudAPIs.Insert import *
from CloudAPIs.Query import *
from CloudAPIs.Edit import *

# from Insert import *
# from Query import *
# from Edit import *

## start with the insert functions
class insert():

    # the account number will be automatically assigned on insertion
    user_info_template = {
        "AccountNumber" : None,
        "Username" : 'str',
        "Email" : 'str',
        "PhoneNumber" : 'int',
        "Fname" : "str",
        "Minit" : "char",
        "Lname" : 'str',
        "UserDoB" : 'yyyy-mm-dd',
        "PasswordHash" : 'str'
    }

    # VideoLink, Thumbnail, UploadDate are automatically assigned on insert
    video_info_template = {
        "VideoID" : None,
        "VideoLink" : None,
        "AccountNumber" : 'int',
        "VideoTitle" : 'str',
        "VidDescription" : 'str',
        "Category" : "dev",
        "Views" : 0,
        "UploadDate" : None,
        "Thumbnail" : None
    }

    comment_info_template = {
        "CommentID" : None,
        "AccountNumber" : 'int',
        "CommentBody" : 'str',
        "PostDate" : None,
        "VideoComment" : 'int',
        "ContentComment" : 'int',
        "ThreadParent" : 'int',
        "Edited" : False
    }

    # SentStamp, AttatchedLink are automatically assigned on insert
    message_info_template = {
        "PairID" : 'int',
        "MessageID" : None,
        "MessageBody" : 'str',
        "SentStamp" : None,
        "SentUser" : 'int',
    }

    friend_info_template = {
        "PairID" : None,
        "User1ID" : 'int',
        "User2ID" : 'int'
    }

    friend_request_info_template = {
        "RequestID" : None,
        "User1ID" : 'int',
        "User2ID" : 'int',
        "User1Accepted" : 'bool',
        "User2Accepted" : 'bool'
    }

    message_info_template = {
        "PairID" : 'int',
        "MessageID" : None,
        "MessageBody" : 'str',
        "SentStamp" : None,
        "SentUser" : 'int',
        "AttatchedLink" : None
    }

    community_info_template = {
        "CommunityID" : None,
        "CommName" : 'str',
        "CommDescription" : 'str',
        "CreatedUser" : 'int'
    }

    community_messages_info_template = {
        "CommunityID" : 'int',
        "MessageID" : None,
        "MessageBody" : 'str',
        "AttatchedLink" : 'str',
        "SentStamp" : None,
        "SentUser" : 'int'
    }

    events_info_template = {
        "EventID" : None,
        "EventName" : 'str',
        "EventDesc" : 'str',
        "PostTime" : None,
        "StartTime" : 'datetime',
        "EventLocation" : 'str',
        "PosterID" : 'int',
        "Category" : 'str'
    }

    def new_user(user_info):
        newAccountInsert(user_info)
        return

    def new_video(video_info):
        newVideoInsert(video_info)
        return

    def new_content_comment(comment_info):
        newCommentInsertContent(comment_info)
        return
    def new_video_comment(comment_info):
        newCommentInsertVideo(comment_info)
        return

    def new_content(content_info):
        newContentInsert(content_info)
        return

    def add_friends(friend_info):
        newFriendsInsert(friend_info)
        return

    def new_message(message_info):
        newFriendMessages(message_info)
        return

    def new_message_link(message_info,link):
        newFriendMessages(message_info,link)
        return

    def new_community(community_info):
        newCommunityInsert(community_info)
        return

    def new_comm_message(message_info):
        newCommMessages(message_info)
        return

    def new_comm_message(message_info,link):
        newCommMessages(message_info,link)
        return

    def new_event(event_info):
        newEvent(event_info)
        return

## query functions
class query():

    # given an account number, returns the row containing the account number
    def account_info(account_number):
        cursor = accountInfo(account_number)
        return cursor
    # given an account number, returns the email associated
    def account_email(account_number):
        cursor = accountSearchEmail(account_number)
        return cursor

    # given an account number, returns a table containing all videos by the specified account
    # ordered descending and ascending by date
    def account_videos_date_desc(account_number):
        cursor = accountVideosDate(account_number, " DESC")
        return cursor
    def account_videos_date_asc(account_number):
        cursor = accountVideosDate(account_number, "")
        return cursor
    
    # given a search term, returns a cursor containing the video(s)
    def search_videos_name(search_term):
        cursor = videoSearchName(search_term)
        return cursor

    # given an account number, returns a table containing all content by the specified account
    # ordered descending and ascending by date
    def account_content_date_desc(account_number):
        cursor = accountContentDate(account_number, " DESC")
        return cursor
    def account_content_date_asc(account_number):
        cursor = accountContentDate(account_number, "")
        return cursor
    
    def friend_messages_date(pair_id):
        cnx,cursor = friendPairMessages(pair_id)
        return cnx,cursor
    
    # given a video/content id, returns a table containing all top-level comments on the specified video/content
    # ordered descending and ascending by date
    # 1 specifies videos for the server-level api, 0 specifies content
    def video_comments_asc(videoid):
        cursor = commentsUnderPost(videoid, "",1)
        return cursor
    def video_comments_desc(videoid):
        cursor = commentsUnderPost(videoid," DESC",1)
        return cursor

    def content_comments_asc(contentid):
        cursor = commentsUnderPost(contentid, "",0)
        return cursor
    def content_comments_desc(contentid):
        cursor = commentsUnderPost(contentid, " DESC",0)
        return cursor
    
    def comment_body(commentid):
        cursor = commentBody(commentid)
        return cursor

## edit functions, for editable tables and columns
    
class edit():
    def video_title(videoid,newtitle):
        videoTitle(videoid,newtitle)
        return 
    def video_description(videoid,newdescription):
        videoDescription(videoid,newdescription)
        return
    
    def comment_body(commentid,newbody):
        commentBody(commentid,newbody)
        return
    
    def content_body(contentid,newbody):
        contentBody(contentid,newbody)
        return

## delete functions for deleteable tables and columns

class delete():
    def de():
        pass
##
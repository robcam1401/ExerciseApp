from Insert import *
from Query import *

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
        "UserDoB" : 'yyyy-mm-dd'
    }

    # VideoLink, Thumbnail, UploadDate are automatically assigned on insert
    video_info_template = {
        "VideoID" : None,
        "AccountNumber" : 'int',
        "Video Title" : 'str',
        "VidDescription" : 'str',
        "Category" : "dev",
        "Views" : 0
    }

    # SentStamp, AttatchedLink are automatically assigned on insert
    message_info_template = {
        "PairID" : 'int',
        "MessageID" : 'int',
        "MessageBody" : 'str',
        "SentStamp" : None,
        "SentUser" : 'int',
    }

    friend_info_template = {
        "PairID" : None,
        "User1ID" : 'int',
        "User2ID" : 'int'
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

    def new_message(message_info,link):
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

    # given an account number, returns a table containing all videos by the specified account
    # ordered descending and ascending by date
    def account_videos_date_desc(account_number):
        cursor = accountVideosDate(account_number, " DESC")
        return cursor
    def account_videos_date_asc(account_number):
        cursor = accountVideosDate(account_number, "")
        return cursor
    
    # given an account number, returns a table containing all content by the specified account
    # ordered descending and ascending by date
    def account_content_date_desc(account_number):
        cursor = accountContentDate(account_number, " DESC")
        return cursor
    def account_content_date_asc(account_number):
        cursor = accountContentDate(account_number, "")
        return cursor
    
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
    
    def commentBody(videoid):
        cursor = commentBody(videoid)
        return cursor

## edit functions, for editable tables and columns
    
class edit():
    def video_title():

        return 

## delete functions for deleteable tables and columns

class delete():
    def de():
        pass
##
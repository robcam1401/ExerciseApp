from Insert import *
from Query import *

## start with the insert functions
class insert():

    def new_user(user_info):
        newAccountInsert(user_info)
        return

    def new_video(video_info):
        newVideoInsert(video_info)
        return

    def new_content_comment(message_info):
        newCommentInsertContent(message_info)
        return
    def new_video_comment(message_info):
        newCommentInsertVideo(message_info)
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

    def accountInfo(account_number):
        cursor = account_info(account_number)
        return cursor

    def account_videos_date_desc(account_number):
        cursor = account_videos_date(account_number, " DESC")
        return cursor
    def account_videos_date_asc(account_number):
        cursor = account_videos_date(account_number, "")
        return cursor
    
    def account_content_date_desc(account_number):
        cursor = account_content_date(account_number, " DESC")
        return cursor
    def account_content_date_asc(account_number):
        cursor = account_content_date(account_number, "")
        return cursor
    
    def video_comments_asc(videoid):
        cursor = comments_under_post(videoid, "")
        return cursor
    def video_comments_desc(videoid):
        cursor = comments_under_post(videoid," DESC")
        return cursor

    def content_comments_asc(contentid):
        cursor = comments_under_post(contentid, "")
        return cursor
    def content_comments_desc(contentid):
        cursor = comments_under_post(contentid, " DESC")
        return cursor
    
    def commentBody(videoid):
        cursor = comment_body(videoid)
        return cursor

## edit functions, for editable tables and columns
    
class edit():
    def e1():
        pass

## delete functions for deleteable tables and columns

class delete():
    def de():
        pass
##
from Insert import connect
## useful queries for the database

# returns all information about a specified account
def account_info(acct_num):
    cnx,cursor = connect()

    query = ("SELECT * FROM UserAccount\
             WHERE AccountNumber = {}").format(acct_num)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def account_search_name(search_term):
    cnx,cursor = connect()

    query = ("SELECT * FROM UserAccount\
             WHERE Username = {}").format(search_term)
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

# returns all videos posted by a single account
# ordered by date, descending or ascending, chosen by calling function
def account_videos_date(acct_num, sort):
    cnx,cursor = connect()

    query = ("SELECT * FROM Videos\
             WHERE AccountNumber = {}\
             ORDER BY UploadDate{}").format(acct_num, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def account_content_date(acct_num, sort):
    cnx,cursor = connect()

    query = ("SELECT * FROM Content\
             WHERE AccountNumber = {}\
             ORDER BY UploadDate{}").format(acct_num, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def video_search_name(search_term):
    cnx, cursor = connect()

    query = ("SELECT * FROM Videos\
             WHERE VideoTitle = {}").format(search_term)
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

# returns IDs of all top-level comments under a post
def comments_under_post(video_id,sort):
    cnx,cursor = connect()

    query = ("SELECT CommentID FROM Content\
             WHERE AccountNumber = {}, ThreadParent = 0\
             ORDER BY PostDate{}").format(video_id, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def comment_body(comment_id):
    cnx,cursor = connect()

    query = ("SELECT CommentBody FROM Comments\
             WHERE CommentID = {}").format(comment_id)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor
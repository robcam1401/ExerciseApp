from Insert import connect
## useful queries for the database

# returns all information about a specified account
def accountInfo(acct_num):
    cnx,cursor = connect()

    query = ("SELECT * FROM UserAccount\
             WHERE AccountNumber = {}").format(acct_num)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def accountSearchName(search_term):
    cnx,cursor = connect()

    query = ("SELECT * FROM UserAccount\
             WHERE Username = {}").format(search_term)
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

# returns all videos posted by a single account
# ordered by date, descending or ascending, chosen by calling function
def accountVideosDate(acct_num, sort):
    cnx,cursor = connect()

    query = ("SELECT * FROM Videos\
             WHERE AccountNumber = {}\
             ORDER BY UploadDate{}").format(acct_num, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def accountContentDate(acct_num, sort):
    cnx,cursor = connect()

    query = ("SELECT * FROM Content\
             WHERE AccountNumber = {}\
             ORDER BY UploadDate{}").format(acct_num, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def videoSearchName(search_term):
    cnx, cursor = connect()

    query = ("SELECT * FROM Videos\
             WHERE VideoTitle = {}").format(search_term)
    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

# returns IDs of all top-level comments under a post
def commentsUnderPost(post_id,sort,post_type):
    cnx,cursor = connect()

    if (post_type == 1):
        query = ("SELECT CommentID FROM Comment\
                WHERE VideoComment = {}, ThreadParent = 0\
                ORDER BY PostDate{}").format(post_id, sort)
    else:
        query = ("SELECT CommentID FROM Comment\
                WHERE ContentComment = {}, ThreadParent = 0\
                ORDER BY PostDate{}").format(post_id, sort)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor

def commentBody(comment_id):
    cnx,cursor = connect()

    query = ("SELECT CommentBody FROM Comments\
             WHERE CommentID = {}").format(comment_id)

    cursor.execute(query)
    cnx.commit()
    cnx.close()
    return cursor
from Insert import connect

def edit_video_title(video_id,new_title):
    cnx,cursor = connect()

    edit = ("UPDATE Videos SET VideoTitle={} WHERE VideoID={}").format(new_title,video_id)
    cursor.execute(edit)
    cnx.commit()

    cursor.close()
    cnx.close()
    return

def edit_video_description(video_id,new_desc):
    cnx,cursor = connect()

    edit = ("UPDATE Videos SET VidDescription={} WHERE VideoID={}").format(new_desc,video_id)
    cursor.execute(edit)
    cnx.commit()
    
    cursor.close()
    cnx.close()
    return

def edit_comment(comment_id,new_comment):
    cnx,cursor = connect()

    edit = ("UPDATE Comments SET CommentBody={} WHERE CommentID={}").format(new_comment,comment_id)
    edit2 = ("UPDATE Comments SET Edited=true WHERE CommentID={}").format(comment_id)
    cursor.execute(edit)
    cnx.commit()
    
    cursor.close()
    cnx.close()

    return


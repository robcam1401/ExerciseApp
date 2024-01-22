import mysql.connector

def connect():
    cnx = mysql.connector.connect(user='GenericUser',host='34.121.87.64',database='ExerciseApp')
    cursor = cnx.cursor()
    return cnx,cursor

# when inserting, columns will be strongly-typed at insert and will be checked to see if they are within the declared parameters
# for example, username is strongly typed as a string and will be checked to see if it is 15 characters or less
def newAccount(username:str, email:str, phone:int, fname:str, minit:str, lname: str,DoB:(int,int,int)):
    if len(username) > 15:
        raise "Username too long"
    if len(email) > 32:
        raise "Email too long"
    if phone > 99999999999:
        raise "Phone number too large"
    if len(fname) > 15:
        raise "First name too long"
    if len(minit) > 1:
        raise "Middle Initial too long"
    if len(lname) > 15:
        raise "Last name too long"
    
    return

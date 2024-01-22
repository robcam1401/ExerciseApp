import Insert
import datetime


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
    cnx,cursor = Insert.connect()
    add_User = ("INSERT INTO UserAccount "
              "(AccountNumber, Username, Email, PhoneNumber,Fname,Minit,Lname,UserDoB)"
              "VALUES (%(AccountNumber)s, %(Username)s, %(Email)s, %(PhoneNumber)s, %(Fname)s, %(Minit)s, %(Lname)s, %(UserDoB)s)")

    data_User = {
        "AccountNumber" : 1,
        "Username" : "Admin",
        "Email" : "user@user.com",
        "PhoneNumber" : 1,
        "Fname" : "Zach",
        "Minit" : "W",
        "Lname" : "Nalepa",
        "UserDoB" : datetime.date(2001,7,20)
    }

    cursor.execute(add_User,data_User)
    cnx.commit()

    cursor.close()
    cnx.close()
    return



ConnectAndQuery()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import bcrypt
import datetime
import mysql.connector 
import configparser

def send_verification_email(user_email, verification_code):
    print(f"Attempting to send verification email to {user_email}...")  # Debugging line
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        sender_email = config['email']['email_user']
        sender_password = config['email']['email_pass']
        subject = "Your Verification Code"
        body = f"Your verification code is: {verification_code}"

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = user_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_email, sender_password)
        text = message.as_string()
        session.sendmail(sender_email, user_email, text)
        print(f"Email sent successfully to {user_email} with code {verification_code}")  # Confirmation print
        session.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred in send_verification_email: {e}")

    
def generate_verification_code():
    return random.randint(100000, 999999)
'''
def store_user_information(user_email, hashed_password, verification_code):
    # Read database configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')  # Ensure the file name matches and is accessible

    # Establish your database connection using the configuration
    db_connection = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['db']
    )
    cursor = db_connection.cursor()

    # Current timestamp
    current_time = datetime.datetime.now()

    # SQL query to insert the new user
    query = "INSERT INTO UserAccount (Username, Email, Password, verification_code, timestamp) VALUES (%s, %s, %s, %s, %s)"
    values = (user_email, hashed_password, verification_code, current_time)

    try:
        cursor.execute(query, values)
        db_connection.commit()
        print("User information stored successfully")  #debuggling line
    except mysql.connector.Error as e:
        print(f"Database error: {e}")   #debugging line
        # Handle database exceptions
    finally:
        cursor.close()
        db_connection.close()
'''

def sign_up_user(user_email):
    verification_code = generate_verification_code()
    
    #sending verificaton email
    send_verification_email(user_email, verification_code)
    #hash the password for security
   # hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
    #database 
    #logic to store the information
   # store_user_information(user_email, hashed_password, verification_code)
 
 #test case   
if __name__ == "__main__":
    test_email = "nabinta21niraula@gmail.com"
    test_code = "123456"
    sign_up_user(test_email, "password123")
    #send_verification_email(test_email, test_code)

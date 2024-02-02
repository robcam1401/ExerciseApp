import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import bcrypt
import datetime
import mysql.connector
import configparser
import secrets  # For generating a secure token

def send_password_reset_email(user_email, reset_token):
    print(f"Attempting to send password reset email to {user_email}...")  # Debugging line
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        sender_email = config['email']['email_user']
        sender_password = config['email']['email_pass']
        password_reset_link = f"https://yourdomain.com/reset-password?token={reset_token}"
        subject = "Password Reset Link"
        body = f"Please click the following link to reset your password: {password_reset_link}"

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
        print(f"Password reset email sent successfully to {user_email}")  # Confirmation print
        session.quit()
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred in send_password_reset_email: {e}")

def generate_reset_token():
    # Generate a secure token that will be hard to guess
    return secrets.token_urlsafe()

'''
def store_reset_token(user_email, reset_token):
    config = configparser.ConfigParser()
    config.read('config.ini')  # Make sure this path is correct
    
    db_connection = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['db']
    )
    cursor = db_connection.cursor()

    # Define an expiration time for the token, e.g., 1 hour from now
    token_expiration = datetime.datetime.now() + datetime.timedelta(hours=1)

    # Get the AccountNumber for the given email
    #cursor.execute("SELECT AccountNumber FROM UserAccount WHERE Email = %s", (user_email,))
    #account_number_result = cursor.fetchone()
    
    #if account_number_result:
    # account_number = account_number_result[0]
    
    # SQL query to insert the new reset token
    query = """
    INSERT INTO PasswordResetRequests (Email, ResetToken, Expiration)
    VALUES (%s, %s, %s)
    """
    values = (user_email, reset_token, token_expiration)

    try:
        cursor.execute(query, values)
        db_connection.commit()
        print("Reset token stored successfully")  # Debugging line
    except mysql.connector.Error as e:
        print(f"Database error: {e}")  # Debugging line
        # Handle database exceptions
    finally:
        cursor.close()
        db_connection.close()

'''

def initiate_password_reset(user_email):
    reset_token = generate_reset_token()
    
    # Store the reset token in the database
    #store_reset_token(user_email, reset_token)
    
    # Send the password reset email with the token
    send_password_reset_email(user_email, reset_token)
    
#tryal   
if __name__ == "__main__":
    test_email = "test@example.com"
    initiate_password_reset(test_email)

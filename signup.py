import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def send_verification_email(user_email, verification_code):
    # Email details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    subject = "Your Verification Code"
    body = f"Your verification code is: {verification_code}"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_email, sender_password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, user_email, text)
    session.quit()
    
def generate_verification_code():
    return random.randint(100000, 999999)

def sign_up_user(user_email, user_password):
    verification_code = generate_verification_code()
    
    #sending verificaton email
    send_verification_email(user_email, verification_code)
    #hash the password for security
    #database 
    #logic to store the information
    
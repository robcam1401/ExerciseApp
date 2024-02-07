import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

def send_test_email():
    # Load email settings from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    sender_email = config['email']['email_user']
    sender_password = config['email']['email_pass']
    receiver_email = "nabinta21niraula@gmail.com"  # Change to your actual receiver email address

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email from Python Script"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = "This is a test email sent from a Python script using SMTP."
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_test_email()

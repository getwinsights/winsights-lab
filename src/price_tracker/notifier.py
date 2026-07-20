import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv


def send_email(subject: str, body: str):

    load_dotenv()

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        
    
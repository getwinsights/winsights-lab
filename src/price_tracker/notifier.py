import smtplib
from email.mime.text import MIMEText


def send_email(subject: str, body: str):

    sender_email = "winnie.reynolds@getwinsights.com"
    app_password = "djmv hanh cgon ngia"
    receiver_email = "winnie.reynolds@getwinsights.com"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
        
    
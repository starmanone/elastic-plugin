import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(html_body):
    """Send an html mail with google gmail"""
    sender_email = "$mail"
    receiver_email = "$mail"
    password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Report from elasticsearc - test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html_body, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

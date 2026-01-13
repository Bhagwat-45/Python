import smtplib,ssl
from settings.settings import settings

def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "app"
    password = settings.gmail_password

    receiver = ""
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
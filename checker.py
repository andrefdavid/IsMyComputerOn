from datetime import datetime
import settings
import smtplib
from email.message import EmailMessage
from time import sleep
import os

def hour_check(current, target):
    if int(current) >= int(target):
        return True
    return False

def checking_cicle():
    now = datetime.now()
    current_hour = now.strftime("%H")
    if hour_check(current_hour, settings.HOUR):
       send_email()
    

    sleep(settings.INTERVAL)

def send_email():
    msg = EmailMessage()
    msg.set_content(settings.EMAIL_CONTENT.format(datetime.now().strftime("%H:%M:%S:")))
    msg['Subject'] = settings.EMAIL_SUBJECT.format(os.environ['COMPUTERNAME'], datetime.now().strftime("%H:%M:%S:"))
    msg['To'] = settings.EMAIL_RECIPIENTS
    msg['From'] = settings.EMAIL_FROM
    server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
    #server.ehlo()
    #server.starttls()
    server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()

while True:
    checking_cicle()

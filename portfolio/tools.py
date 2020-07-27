from config import Config
from email.message import EmailMessage
from random import randint
from datetime import datetime
import smtplib, urllib, json, time, re, os

if Config.RUN_MODE == "dev":
    print(">>>", os.path.basename(__file__))

def send_email(addr: str, test=False) -> str: # Return token string
    token = get_reset_password_token()
    if not test:
        msg = EmailMessage()
        msg.set_content(f"\
    <html><body>Dear user,<br>\
    <br>To reset your password click <a href=\"http://localhost:5000/reset_password/{token}\">here</a></br>\
    <br>Alternatively, you can paste the following link in your browser's address bar:</br>\
    <br>http://localhost:5000/reset_password/{token}</br>\
    <br>If you have not requested a password reset simply ignore this message.</br>\
    <br>Sincerely,</br><br>Team BCT</br></body></html>", subtype="html")
        msg["Subject"] = "Password Reset Requested - EquIP"
        msg["From"] = Config.MAIL_USERNAME
        msg["To"] = addr
        with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT) as s:
                s.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
                s.send_message(msg)
    return token

def send_post(route, data={}):
    url = Config.DOMAIN + '/' + str(route.strip('/'))
    data_encoded = urllib.parse.urlencode(data)
    data_encoded = data_encoded.encode("ascii")
    resp = urllib.request.urlopen(url, data_encoded)
    return resp.read().decode()

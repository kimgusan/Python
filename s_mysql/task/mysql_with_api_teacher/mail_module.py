# 구글 앱 비밀번호 : blcu xhlg oksu jrla

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 맥북은 아래의 명령어를 반드시 작성한다.
# ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl

def send_email(member_phone, certification_number):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "kimkyusan94@gmail.com"
    receiver_email = "kimkyusan94@gmail.com"
    password = "blcu xhlg oksu jrla"
    message = "<h1>내용</h1>"

    msg = MIMEText(message, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, data.as_string())
import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호 뭐니? : ')

email_list = ['jiseon9425@hanmail.net','wiahawm7@gmail.com']

for email in email_list:

    msg = EmailMessage()
    msg['Subject'] = "제목이다"
    msg['From'] = "wia_hawm@naver.com"
    msg['To'] = email #jiseon9425@hanmail.net, wiahawm7 두번의 메세지 보냄
    msg.set_content('내용이다')
    
    smtp_url = 'smtp.naver.com'
    smtp_port = 465
    
    s = smtplib.SMTP_SSL(smtp_url, smtp_port)
    
    s.login('wia_hawm',password)
    s.send_message(msg)
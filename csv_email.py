import csv

import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호 뭐니? : ')

smtp_url = 'smtp.naver.com'
smtp_port = 465
    
s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('wia_hawm',password)

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)

for line in read_csv:

    msg = EmailMessage()
    msg['Subject'] = "저는 이지선입니다."
    msg['From'] = "wia_hawm@naver.com"
    msg['To'] = line[1]
    msg.set_content('저는'+line[0]+'님께 보냈습니다.')
    
    s.send_message(msg)
    
    
f.close()


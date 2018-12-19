import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호 뭐니? : ')

msg = EmailMessage()
msg['Subject'] = "란찡은 배고프다"
msg['From'] = "wia_hawm@naver.com"
msg['To'] = "sosp32@daum.net"
#msg.set_content('내용입니다')
msg.add_alternative('''
<h1>안녕하세요!!</h1>
<p> 하하하하 움하하하</p>
''',subtype="html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)

s.login('wia_hawm',password)
s.send_message(msg)
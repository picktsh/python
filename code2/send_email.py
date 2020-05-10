import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = input('请输入你的邮箱：')
password = input('请输入你的密码：')
to_addr = input('请输入收件人的邮箱：')


def send_email(content, subject):
    smtp_server = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(smtp_server, 587)
    qqmail.login(from_addr, password)
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(from_addr, to_addr, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()


content = "吃个锤子"
subject = "周末吃什么?"
send_email(content, subject)

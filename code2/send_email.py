import smtplib
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')


def send_email(content, subject):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = content
    message = MIMEText(content, 'plain', 'utf-8')
    subject = subject
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

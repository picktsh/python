import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 引入smtplib、MIMEText和Header

mailhost = 'smtp.qq.com'
# 把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
qqmail = smtplib.SMTP()
# 实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
qqmail.connect(mailhost, 25)
# 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
# 以上，皆为连接服务器。

account = input('请输入你的邮箱：')
# 获取邮箱账号，为字符串格式
password = input('请输入你的密码：')
# 获取邮箱密码，为字符串格式
qqmail.login(account, password)
# 登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
# 以上，皆为登录邮箱。

receiver = input('请输入收件人的邮箱：')
# 获取收件人的邮箱。

content = input('请输入邮件正文：')
# 输入你的邮件正文，为字符串格式
message = MIMEText(content, 'plain', 'utf-8')
# 实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码
subject = input('请输入你的邮件主题：')
# 输入你的邮件主题，为字符串格式
message['Subject'] = Header(subject, 'utf-8')
# 在等号的右边是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
# 以上，为填写主题和正文。

try:
    qqmail.sendmail(account, receiver, message.as_string())
    print('邮件发送成功')
except:
    print('邮件发送失败')
qqmail.quit()
# 以上为发送邮件和退出邮箱。

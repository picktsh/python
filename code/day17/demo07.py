"""
第二种方法是采用询问“是否继续输入邮箱地址”的方式，并用while循环来实现多个收件人的功能。
"""

# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 收信方邮箱
to_addrs = []
while True:
    a = input('请输入收件人邮箱：n退出')
    # b = input('是否继续输入，n退出，任意键继续：')
    if a == 'n':
        break
    to_addrs.append(a)

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的学员，你好！
我是吴枫老师，能遇见你很开心。
希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text, 'plain', 'utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()

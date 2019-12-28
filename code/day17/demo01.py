import smtplib

host = 'smtp.qq.com'  # 主机
port = 25  # 端口 (25,465)
username = 'xxx@qq.com'  # 登录邮箱的用户名
password = '你的授权码数字'  # 授权码
from_addr = ''  # 邮件发送地址，就是上面的username
to_addr = ''  # 邮件收件人地址

server = smtplib.SMTP()
server.connect(host, port)

# server = smtplib.SMTP_SSL()
# 如果端口是用SSL加密，请这样写代码。其中server是变量名
# server.connect(host, 465)
# 如果出现编码错误UnicodeDecodeError，你可以这样写：server.connect('smtp.qq.com', 465,'utf-8')

# username:登录邮箱的用户名
# password：授权码
server.login(username, password)
server.sendmail(from_addr, to_addr, msg.as_string())
# msg.as_string()：为一个字符串类型;
server.quit()

server = smtplib.SMTP_SSL()
# 如果端口是用SSL加密，请这样写代码。其中server是变量名
server.connect('smtp.qq.com', 465)
# 如果出现编码错误UnicodeDecodeError，你可以这样写：server.connect('smtp.qq.com', 465,'utf-8')

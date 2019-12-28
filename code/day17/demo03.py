# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText

# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '1134512154@qq.com'
password = 'avsfycehkbgghcac'

# 收信方邮箱
to_addr = '1134512154@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# msg：文本内容，可自定义
# type：文本类型，默认为plain（纯文本）
# chartset：文本编码，中文为“utf-8”
content = 'send by python'
# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText(content, 'plain', 'utf-8')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()

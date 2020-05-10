import smtplib

# smtplib是python的一个内置库，所以不需要用pip安装
mailhost = 'smtp.qq.com'
# 把qq邮箱的服务器地址赋值到变量mailhost上，地址需要是字符串的格式。
qqmail = smtplib.SMTP()
# 实例化一个smtplib模块里的SMTP类的对象，这样就可以使用SMTP对象的方法和属性了
qqmail.connect(mailhost, 25)
# 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。

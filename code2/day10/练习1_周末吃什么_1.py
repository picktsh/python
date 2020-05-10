"""
第一步：明确目标
先明确目标：我们曾在第3关爬取了下厨房网站中的“本周最受欢迎菜谱”，现在，我们完善这个程序，让程序在每个周五爬取数据，并把菜谱发送到我们的邮箱。

步骤讲解
先明确目标：我们曾在第3关爬取了下厨房网站中的“本周最受欢迎菜谱”，现在，我们完善这个程序，让程序在每个周五爬取数据，并把菜谱发送到我们的邮箱。
该项目和第10关课堂的项目是非常相似的。
"""
"""
第二步：分析过程
再分析过程：这个程序一共分为三部分：爬虫、通知和定时。

步骤讲解
这个程序一共分为三部分，知识我们都掌握了。
0.爬虫：爬取下厨房网站中本周最欢迎菜谱的菜名、链接、原材料。
1.通知：用smtplib、email库来发送邮件。
2.定时：用schedule和time库定时执行程序。
我们分别写出来，然后封装成函数。
先把每个程序写出来，然后拼装到一起；鉴于爬虫程序已经学过，就直接把代码提供给大家。
"""
"""
第三步：代码实现
接下来就是写代码啦。
0.爬虫：爬虫代码已经在课堂上学过，所以直接把爬虫代码提供给大家，并请大家先封装爬虫代码：
"""
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
url = 'http://www.xiachufang.com/explore/'
res_foods = requests.get(url, headers=headers)
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
list_foods = bs_foods.find_all('div', class_='info pure-u')

list_all = []
for food in list_foods:
    tag_a = food.find('a')
    name = tag_a.text[17:-13]
    URL = 'http://www.xiachufang.com' + tag_a['href']
    tag_p = food.find('p', class_='ing ellipsis')
    ingredients = tag_p.text[1:-1]
    list_all.append([name, URL, ingredients])
print(list_all)
"""
1.邮件：邮件代码是第10关所学的内容，下面提供代码给大家，但最好是回忆不起来再看；写完代码后请大家封装代码。（仍然提醒同学们，学习系统会记录大家输入的内容。考虑到信息隐私的问题，大家不要在这里输入自己的邮箱密码或账号。因此，请你在本地运行邮件相关的代码）
"""
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 引入smtplib、MIMEText和Header
#
# mailhost = 'smtp.qq.com'
# # 把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
# qqmail = smtplib.SMTP()
# # 实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
# qqmail.connect(mailhost, 25)

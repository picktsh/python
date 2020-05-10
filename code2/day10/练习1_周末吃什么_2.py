import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header


def menu_spider():
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
    return list_all


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


def job():
    print('开始一次任务')
    menus = menu_spider()
    # 这里要处理成适合页面显示的文本内容
    page = '<ol>'
    for i in menus:
        page += '<li>{}</li>'.format(i)
    page += '</ol>'
    print(page)
    send_email(page, "周末吃什么?看这里")
    print('任务完成')


# schedule.every().day.at("07:30").do(job)
schedule.every(3).seconds.do(job)  # 每2s执行一次job()函数
while True:
    schedule.run_pending()
    time.sleep(1)

import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')


def weather_spider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    # 天气来源需要 纠正下
    url = 'http://www.weather.com.cn/weather/101280601.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    tem1 = soup.find(class_='tem')
    weather1 = soup.find(class_='wea')
    tem = tem1.text
    weather = weather1.text
    return tem, weather


def send_email(tem, weather):
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = tem + weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()


def job():
    print('开始一次任务')
    tem, weather = weather_spider()
    send_email(tem, weather)
    print('任务完成')


schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

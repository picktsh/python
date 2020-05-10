# 封装获取天气的方法
import requests
from bs4 import BeautifulSoup


def weather_spider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = 'http://www.weather.com.cn/weather/101280601.shtml'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    data1 = soup.find(class_='tem')
    data2 = soup.find(class_='wea')
    tem = data1.text
    weather = data2.text
    return tem, weather

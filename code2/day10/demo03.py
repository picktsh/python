import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://www.weather.com.cn/weather/101280601.shtml'
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, "html.parser")
w_wea = soup.select_one(".c7d ul.t>li .wea")
w_tem = soup.select_one(".c7d ul.t>li .tem")

print("天气:", w_wea.text)
print("温度:", w_tem.text)

# 下面是老师的参考代码
# bsdata = BeautifulSoup(res.text, 'html.parser')
# # 使用bs模块解析获取到的数据
# data1 = bsdata.find(class_='tem')
# # 使用find()取出天气的温度数据
# data2 = bsdata.find(class_='wea')
# # 使用find()取出天气的文字描述
# print(data1.text)
# # 取出变量data1中的字符串内容，并打印
# print(data2.text)
# # 取出变量data2中的字符串内容，并打印

"""
课堂练习
获取数据：选取的URL是：http://www.xiachufang.com/explore/， 接着，使用BeautifulSoup对获取的数据进行解析。

不懂做？点击下面的“需要帮助”。
"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.xiachufang.com/explore/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)
info = soup.find_all("div", class_="info pure-u")
print(info)


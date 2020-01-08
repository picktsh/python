"""
在网页的HTML代码中，有三个div元素（<div></div>），用find()可以提取出首个元素(只有一个)，而find_all()可以全部取出（三个）。
"""
import requests
from bs4 import BeautifulSoup

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
# 使用find()方法提取首个<div>元素，并放到变量item里。
item = soup.find('div')
# 打印item的数据类型
print(type(item))  # <class 'bs4.element.Tag'>
# 打印item
print(item)  # <div>大家好，我是一个块</div>

"""
再来试试find_all()吧，它可以提取出网页中的全部div元素（3个），请看代码（第7行为新增代码），然后点击运行。
"""
items = soup.find_all('div')
# 打印items的数据类型
print(type(items))  # <class 'bs4.element.ResultSet'>
# 打印items
print(items)  # [<div>大家好，我是一个块</div>, <div>我也是一个块</div>, <div>我还是一个块</div>]

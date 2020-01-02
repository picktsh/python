"""
上面的代码是第0关学过的内容，好，接下来就轮到BeautifulSoup登场解析数据了，请特别留意第2行和第6行新增的代码。
"""
import requests
# 引入BS库，下面的bs4就是beautifulsoup4
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')
print(type(html))
print(type(soup))

"""
输出:
<class 'str'>
<class 'bs4.BeautifulSoup'>
"""
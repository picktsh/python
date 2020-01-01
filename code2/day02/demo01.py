"""
课堂练习
获取这个书苑不太冷的网页源代码，并且打印。

URL：https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html

忘记怎么写了？点击下面的"需要帮助"。
"""
import requests

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'

res = requests.get(url)

print(res.text)

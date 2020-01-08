"""
课堂练习
续写下方代码，使用find_all()语法查找最小父级标签，并把查找的结果打印出来。

不懂做？点击下面的“需要帮助”。
"""
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
info = bs_foods.find_all("div", class_="info pure-u")
print(info)

"""
这个，是我提供的参考答案：
"""
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 查找最小父级标签
list_foods = bs_foods.find_all('div', class_='info pure-u')
# 打印最小父级标签
print(list_foods)

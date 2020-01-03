"""
课堂练习
续写下方代码，提取出第0个父级标签中的第0个<a>标签，并输出菜名和URL。

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
# 查找最小父级标签
list_foods = bs_foods.find_all('div', class_='info pure-u')
first_a = list_foods[0].find('a')
print(first_a)
"""
参考代码
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

# 提取第0个父级标签中的<a>标签
tag_a = list_foods[0].find('a')
# 输出菜名，使用[17:-13]切掉了多余的信息
print(tag_a.text[17:-13])
# 输出URL
print('http://www.xiachufang.com' + tag_a['href'])

"""
课堂练习
续写代码：写一个循环，提取当前页面的所有菜名、URL、食材，并将它存入列表。其中每一组菜名、URL、食材是一个小列表，小列表组成一个大列表。

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

# 提取第0个父级标签中的<a>标签
tag_a = list_foods[0].find('a')
# 菜名，使用[17:-13]切掉了多余的信息
name = tag_a.text[17:-13]
# 获取URL
URL = 'http://www.xiachufang.com' + tag_a['href']

# 提取第0个父级标签中的<p>标签
tag_p = list_foods[0].find('p', class_='ing ellipsis')
# 食材，使用[1:-1]切掉了多余的信息
ingredients = tag_p.text[1:-1]

list = []
for i in list_foods:
    food = {}
    tag_a = i.find('a')
    food["name"] = tag_a.text[17:-13]
    food['URL'] = 'http://www.xiachufang.com' + tag_a['href']
    food['ingredients'] = i.find('p', class_='ing ellipsis').text[1:-1]
    list.append(food)
print(list)
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

# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com' + tag_a['href']
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('p', class_='ing ellipsis')
    # 食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name, URL, ingredients])

# 打印
print(list_all)

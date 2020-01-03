"""
课堂练习
请你在之前代码的基础上，写出提取食材的代码，并打印出来。

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
ing = list_foods[0].find('p', class_="ing ellipsis").text
print(ing)
# 牛奶、低筋面粉、鸡蛋、细砂糖

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
# 菜名，使用[17:-13]切掉了多余的信息
name = tag_a.text[17:-13]
# 获取URL
URL = 'http://www.xiachufang.com' + tag_a['href']

# 提取第0个父级标签中的<p>标签
tag_p = list_foods[0].find('p', class_='ing ellipsis')
# 食材，使用[1:-1]切掉了多余的信息
ingredients = tag_p.text[1:-1]
# 打印食材
print(ingredients)

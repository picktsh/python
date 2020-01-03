"""
课堂练习
换一种思路写代码：我们分别提取所有的菜名、所有的URL、所有的食材。然后让菜名、URL、食材给一一对应起来。

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

# 查找包含菜名和URL的<p>标签
tag_name = bs_foods.find_all('p', class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_foods.find_all('p', class_='ing ellipsis')
# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表。注意下面[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_food = [tag_name[x].text[18:-14], tag_name[x].find('a')['href'], tag_ingredients[x].text[1:-1]]
    # 将信息添加进list_all
    list_all.append(list_food)
# 打印
print(list_all)

## BeautifulSoup实践 解密吴氏私厨

> 1. 复习
> 2. 项目：解密吴氏私厨

我写过一段Python代码，它能在每个周五爬取最新出的热门菜谱清单，发送到我的邮箱。内含：菜名、原材料、详细烹饪流程的URL。

> 3. 分析过程

在这个项目里，我们选取的网站是“下厨房”。它有一个固定栏目，叫做“本周最受欢迎”，收集了当周最招人喜欢的菜谱。地址如下：

http://www.xiachufang.com/explore/

在进行爬取之前，我们先去看看它的robots协议。网址在此：

http://www.xiachufang.com/robots.txt

刚刚打开Elements，它会默认展开body，其余都关闭。我的鼠标悬停在`<div class="page-outer">…<div>` 上，所以你看到下方限制的路径，就是：`html > body > div.page-outer`。其中.所代表的正是`class`。

如此，我们就定位到了菜名的所在位置，<a>标签内的文本，甚至还顺带找到了详情页URL的所在位置。如上图，<a>标签里有属性href，其值是/recipe/103646251/。点击它，你会跳转到这道菜的详情页：

http://www.xiachufang.com/recipe/103646251/

所以到时候，我们可以去提取<a>标签。接着，先用text拿到它的文本，再使用[href]获取到半截URL，和http://www.xiachufang.com)做拼接即可。

小孩子才做选择，大人们则是全都要。下面，我们会详细介绍思路一，而把思路二留给你做练习。

在最后，提取到了数据我们要存储。但文件存储我们要到第6关才学习。所以，我们就先把数据存到列表里：每一组菜名、URL、食材是一个小列表，小列表组成一个大列表。如下：
```
[[菜A,URL_A,食材A],[菜B,URL_B,食材B],[菜C,URL_C,食材C]]
```


> 4. 代码实现(一)
- 获取与解析
- 提取最小父级标签
- 一组菜名,url,食材
- 写循环,存列表
> 5. 代码实现(二)
> 6. 复习总结

这说明，我们找的规律没错。那么基于此，我们可以产生两种写爬虫的思路：

思路一：我们先去爬取所有的最小父级标签<div class="info pure-u">，然后针对每一个父级标签，想办法提取里面的菜名、URL、食材。
```python
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
```

```python
from bs4 import BeautifulSoup

bs = BeautifulSoup('<p><a>惟有痴情难学佛</a>独无媚骨不如人</p>','html.parser')
tag = bs.find('p')
print(tag.text)
```

```python
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='info pure-u')

# 创建一个空列表，用于存储信息
list_all = []

for food in list_foods:
    # 提取第0个父级标签中的<a>标签
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com'+tag_a['href']
    # 提取第0个父级标签中的<p>标签
    tag_p = food.find('p',class_='ing ellipsis')
    # 食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name,URL,ingredients])

# 打印
print(list_all)
```

思路二：我们分别提取所有的菜名、所有的URL、所有的食材。然后让菜名、URL、食材给一一对应起来（这并不复杂，第0个菜名，对应第0个URL，对应第0组食材，按顺序走即可）。
```python
# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')

# 查找包含菜名和URL的<p>标签
tag_name = bs_foods.find_all('p',class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
# 创建一个空列表，用于存储信息
list_all = []
# 启动一个循环，次数等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表。注意下面[18:-14]切片和之前不同，是因为此处使用的是<p>标签，而之前是<a>
    list_food = [tag_name[x].text[18:-14],tag_name[x].find('a')['href'],tag_ingredients[x].text[1:-1]]
    # 将信息添加进list_all    
    list_all.append(list_food)
# 打印
print(list_all)
```

```
from bs4 import BeautifulSoup

bs = BeautifulSoup('<p><a>惟有痴情难学佛</a>独无媚骨不如人</p>','html.parser')
tag = bs.find('p')
print(tag.text)
```









"""
现在，三本书的全部信息都被我们提取出来了。它的数据类型是<class 'bs4.element.ResultSet>， 前面说过可以把它当做列表list来看待。

不过，列表并不是我们最终想要的东西，我们想要的是列表中的值，所以要想办法提取出列表中的每一个值。

用for循环遍历列表，就可以把这三个div元素取出来了。
"""
# 调用requests库
import requests
# 调用BeautifulSoup库
from bs4 import BeautifulSoup

# 返回一个Response对象，赋值给res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 把Response对象的内容以字符串的形式返回
html = res.text
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')
# 通过定位标签和属性提取我们想要的数据
items = soup.find_all(class_='books')
for item in items:
    # 打印item
    print('想找的数据都包含在这里了：\n', item)
    
    """
    我们一般会选择用type()函数查看一下数据类型，因为Python是一门面向对象编程的语言，只有知道是什么对象，才能调用相关的对象属性和方法。
    """
    print(type(item))  # <class 'bs4.element.Tag'>

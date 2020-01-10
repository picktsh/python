"""
要求：
在本练习，我们会借助cookies的相关知识，使用Python登录小说网站，用代码的形式对热榜上的小说进行推荐。

网站地址：https://www.xslou.com/
"""
"""
目的：
练习掌握cookies和session的用法
练习post和get请求
练习json数据的解析提取
反爬虫应对策略
"""
"""
1 题目要求
项目目标：在本练习，我们会借助cookies的相关知识，使用Python登录小说楼，爬取热榜小说，对小说进行推荐。
网站地址：https://www.xslou.com/
"""
"""
步骤讲解
在本练习，我们会借助cookies的相关知识，使用Python登录小说楼，爬取热榜小说，对小说进行推荐。

网站地址：https://www.xslou.com/
"""
"""
3 代码实现
"""
# 小说楼登录请求：https://www.xslou.com/login.php

import requests
import bs4

# 创建会话。
session = requests.session()
# 登录的网址。
url = 'https://www.xslou.com/login.php'
# 添加请求头，避免被反爬虫。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 登录的参数。
data = {
    # 'username': input('请输入你的账号:'),
    # 'password': input('请输入你的密码:'),
    'username': 'dear001',
    'password': 'a123456',
    'action': 'login',
}

# 在会话下，用post发起登录请求。
res = session.post(url, headers=headers, data=data)
# print(res.content.decode('gbk'))
# print(res.encoding)
if res.status_code == 200:
    bs = bs4.BeautifulSoup(res.content.decode('gbk'), 'html.parser')
    target = bs.find('div', class_='blocktitle')
    # print(target.text)
    if target.text == '登录成功':
        print('登陆成功,继续下一步操作')
else:
    print('请求失败:', url)

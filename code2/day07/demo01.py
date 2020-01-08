# 引入request和bs
import requests
from bs4 import BeautifulSoup

# 使用headers是一种默认的习惯，默认你已经掌握啦~
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 发起请求，将响应的结果赋值给变量res。
url = 'https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=1'
res = requests.get(url, headers=headers)
# 检查状态码
print(res.status_code)
# 打印网页源代码
print(res.text)
# 用bs进行解析
bstitle = BeautifulSoup(res.text, 'html.parser')
# 提取我们想要的标签和里面的内容
title = bstitle.find_all(class_='ContentItem-title')
# 打印title
print(title)

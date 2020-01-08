"""
写代码~

复习了所有知识点，一切都准备就绪，那就开始写代码吧！

你需要爬取的是博客【人人都是蜘蛛侠】中，《未来已来（四）——Python学习进阶图谱》文章的默认评论页，并且打印。

文章URL:

https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/
"""
import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
# 使用select()方法查询当前页评论的列表
item = soup.select('#comments .comment-list .comment')
# 打印item的数据类型
print(type(item), len(item))
for i in item:
    author = i.select(".comment-author .fn")[0].text.replace("\t", "").replace("\n", "")
    date = i.select(".comment-metadata time")[0].text.replace("\t", "").replace("\n", "")
    content = i.select(".comment-content p")[0].text.replace("\t", "").replace("\n", "")
    print("作者:{},评论时间:{},评论内容:{}".format(author, date, content))

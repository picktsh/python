"""
练习介绍
你已经学习了用bs库解析数据和提取数据的方法，也做了豆瓣电影top250的爬取练习，现在我们一起试试下载电影吧٩̋(๑˃́ꇴ˂̀๑)

要求：
实现功能：用户输入喜欢的电影名字，程序即可在电影天堂https://www.ygdy8.com爬取电影所对应的下载链接，并将下载链接打印出来。
"""
"""
第一步：分析问题，明确目标

我们想要实现这样的功能：用户输入喜欢的电影名字，程序即可在电影天堂https://www.ygdy8.com爬取电影所对应的下载链接，并将下载链接打印出来。
"""
"""
步骤讲解
我们知道爬虫是模拟人在浏览器的动作批量获取有价值的信息，那对于这道题，我们先手动操作下，看看人是如何实现这个过程的。

首先，打开电影天堂https://www.ygdy8.com ， 在”搜索“处，填写一部电影名，以”无名之辈“为例，
"""
# from urllib.parse import quote
#
# a = '无名之辈'
# b = a.encode('gbk')
# # 将汉字，用gbk格式编码，赋值给b
# print(quote(b))  # %CE%DE%C3%FB%D6%AE%B1%B2
# # quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
"""
第二步：分析讲解

“输名字 - 查搜索结果 - 进入下载页面 - 找到下载链接”
我们是这样找到下载链接的，那只要让我们的爬虫也走这样的步骤， 就可以达成我们的目标啦～

步骤讲解
步骤一
“输名字”，学过基础课的同学一定可以想到，用input()就可以啦。
步骤二
”搜索结果页面“ 这里面涉及到一个坑，我们要一起填上。
输入不同的电影名，观察搜索结果页面的URL：
《无名之辈》的搜索结果URL：http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=%CE%DE%C3%FB%D6%AE%B1%B2
《神奇动物》的搜索结果URL：http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=%C9%F1%C6%E6%B6%AF%CE%EF
《狗十三》 的搜索结果URL：http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=%B9%B7%CA%AE%C8%FD
观察URL，不难发现：http://s.ygdy8.com/plus/s0.php?typeid=1&keyword= 这些都是一样的，只不过不同的电影名对应URL后面加了一些我们看不懂的字符，
请阅读以下代码，注意注释哦：

记得在本地IDE上试着敲下哦，可以把‘无名之辈’换成神奇动物和狗十三，看看输出结果是否和对应的编码一致。
诶，发现的确是一致的，那我们一起来解读这段代码是怎么实现的呢。
注释中提到了gbk格式编码，那gbk是什么呢？
GBK编码
GBK是中国标准，只在中国使用，并没有表示大多数其它国家的编码；
而各国又陆续推出各自的编码标准，互不兼容，非常不利于全球化发展。
于是后来国际组织发行了一个全球统一编码表，把全球各国文字都统一在一个编码标准里，名为Unicode。
由此我们知道，想把中文转换成url格式，需要先用encode('gbk')将其转成gbk编码，然后再用quote()把它转化成url的一部分。
然后再将它与http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=拼接起来就是电影的搜索结果页面啦～
好，总结下上面的这个知识点，如何建立“输入电影名”与“搜索结果页面”的联系：

中文 - gbk - url - 拼接

这样我们就把完整的搜索结果页面找到并提取出来了。
步骤三 + 步骤四
”进入下载页面“ 与 “找到下载链接” 就是解析网页定位啦，利用find() 和 find_all()，都是你会的内容，加油呀～
"""
"""
第三步：书写代码吧 (｡▰‿‿▰｡) ❤

前两步我们已经捋顺了思路，还填了一个小坑，现在要自己敲代码咯，对转换格式编码的代码记不清的同学，可以偷偷看下提示哦。
"""
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

m_name = input("想看什么电影?请输入电影名后按回车")
# 无名之辈

url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword={}'.format(quote(m_name.encode('gbk')))
print("搜索链接:" + url)
res = requests.get(url, headers=headers)
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    # 获取解析结果
    # try:
    tag = soup.select(".co_area2 .co_content8 a")
    # tag[0]['href']  # /html/gndy/dyzz/20190104/58016.html
    m_url = 'https://www.ygdy8.com{}'.format(tag[0]['href'])
    print("电影链接:" + m_url)
    res = requests.get(m_url, headers=headers)
    encoding = res.encoding
    soup = BeautifulSoup(res.text, 'html.parser')
    ftpUrl = soup.select("#Zoom span table tbody tr td a")
    print('磁力链下载点击这里:{}'.format(ftpUrl[0].text.encode(encoding)))
    # except:
    #     print('抱歉没搜到想要的内容')

else:
    print("请求失败了")
print('程序结束')

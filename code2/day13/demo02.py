# 按照过去的知识，我们可能会把代码写成这个模样：
import scrapy
import bs4
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    # 定义一个爬虫类DoubanSpider。
    name = 'douban'
    # 定义爬虫的名字为douban。
    allowed_domains = ['book.douban.com']
    # 定义爬虫爬取网址的域名。
    start_urls = []
    # 定义起始网址。
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)
        # 把豆瓣Top250图书的前3页网址添加进start_urls。

    def parse(self, response):
        # parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用BeautifulSoup解析response。
        datas = bs.find_all('tr', class_="item")
        # 用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
        for data in datas:
            # 遍历data。
            title = data.find_all('a')[1]['title']
            # 提取出书名。
            publish = data.find('p', class_='pl').text
            # 提取出出版信息。
            score = data.find('span', class_='rating_nums').text
            # 提取出评分。
            print([title, publish, score])
        # 打印上述信息。

import scrapy
import bs4


# 在Scrapy中，每个爬虫的代码结构基本都如下所示：
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self, response):
        print(response.text)

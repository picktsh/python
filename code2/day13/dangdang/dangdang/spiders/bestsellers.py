import scrapy
import bs4
from ..items import DangdangItem


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['http://bang.dangdang.com']
    start_urls = []
    for x in range(1, 4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(x)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        elements = soup.find('ul', class_="bang_list clearfix bang_list_mode").find_all('li')
        for element in elements:
            item = DangdangItem()
            item['name'] = element.find('div', class_="name").find('a')['title']
            item['author'] = element.find('div', class_="publisher_info").text
            item['price'] = element.find('div', class_="price").find('span', class_="price_n").text
            yield item

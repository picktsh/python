"""
就是构造新的requests对象和定义新的方法处理response。
"""
# 导入模块：
import scrapy
import bs4
from ..items import JobuiItem


class JobuiSpider(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    # 提取公司id标识和构造公司招聘信息的网址：
    def parse(self, response):
        # parse是默认处理response的方法
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        ul_list = bs.find_all('ul', class_="textList flsty cfix")
        for ul in ul_list:
            a_list = ul.find_all('a')
            for a in a_list:
                company_id = a['href']
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                yield scrapy.Request(real_url, callback=self.parse_job)

    # 用yield语句把构造好的request对象传递给引擎。用scrapy.Request构造request对象。callback参数设置调用parsejob方法。

    def parse_job(self, response):
        # 定义新的处理response的方法parse_job（方法的名字可以自己起）
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # 用BeautifulSoup解析response(公司招聘信息的网页源代码)
        company = bs.find(id="companyH1").text
        # 用find方法提取出公司名称
        datas = bs.find_all('div', class_="c-job-list")
        # 用find_all提取<div class_="c-job-list">标签，里面含有招聘信息的数据
        for data in datas:
            # 遍历datas
            item = JobuiItem()
            # 实例化JobuiItem这个类
            item['company'] = company
            # 把公司名称放回JobuiItem类的company属性里
            item['position'] = data.find('a').find('h3').text
            # 提取出职位名称，并把这个数据放回JobuiItem类的position属性里
            item['address'] = data.find_all('span')[0]['title']
            # 提取出工作地点，并把这个数据放回JobuiItem类的address属性里
            item['detail'] = data.find_all('span')[1]['title']
            # 提取出招聘要求，并把这个数据放回JobuiItem类的detail属性里
            yield item
            # 用yield语句把item传递给引擎

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy


# 导入scrapy
class DoubanItem(scrapy.Item):
    # 定义一个类DoubanItem，它继承自scrapy.Item
    title = scrapy.Field()
    # 定义书名的数据属性
    publish = scrapy.Field()
    # 定义出版信息的数据属性
    score = scrapy.Field()
    # 定义评分的数据属性

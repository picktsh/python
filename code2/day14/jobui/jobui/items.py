# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    company = scrapy.Field()
    position = scrapy.Field()
    address = scrapy.Field()
    detail = scrapy.Field()

# scrapy.Field()这行代码实现的是，让数据能以类似字典的形式记录
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
book = DoubanItem()
# 实例化一个DoubanItem对象
book['title'] = '海边的卡夫卡'
book['publish'] = '[日] 村上春树 / 林少华 / 上海译文出版社 / 2003'
book['score'] = '8.1'
print(book)
print(type(book))

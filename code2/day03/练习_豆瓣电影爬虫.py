"""
练习介绍：
经典电影知多少
周末夜晚，我们解锁了吴氏私厨，再来看部经典影片来享受闲暇好时光吧 (　･ิω･ิ)ノิ
要说到经典影片，一定要到文艺青年们热爱的豆瓣找一下，看看 TOP250都有哪些呢～
聪明的你可以用两种方法把 序号 /电影名/评分/推荐语/链接 都爬取下来帮助吴枫挑选电影嘛～
"""
"""
1. 第一步：分析问题，明确结果

问题需求就是把豆瓣TOP250里面的 序号/电影名/评分/推荐语/链接 都爬取下来，结果就是全部展示打印出来
"""
"""
第二步：思考要用到的知识

要爬取“序号/电影名/评分/推荐语/链接”这些信息，我们已经学习了用requests.get()获取数据，BeautifulSoup库解析数据，find()和find_all()提取数据，还有呢，观察下，一共10页，我们还要加个for循环对吧～
"""
"""
第三步：书写思路一代码

先爬取最小共同父级标签<li>，然后针对每一个父级标签，提取里面的序号/电影名/评分/推荐语/链接。

注：下方代码仅为思路提示，并非参考答案。
"""
"""
步骤讲解
接下来我们一起分析网页吧～
进入首页 https://movie.douban.com/top250?start=0&filter= ，打开检查工具，在Elements里查看这个网页，是什么结构。点击开发者工具左上角的小箭头，选中“肖申克的救赎”，这样就定位了电影名的所在位置，审查元素中显示<span class="title">：<span>标签内的文本，class属性；推荐语和评分也是如此，<span class='inq'>，<span class='rating_num'>；序号：<em class>，<em>标签内的文本，class属性；推荐语<span class='inq'>；链接是<a>标签里href的值。最后，它们最小共同父级标签，是<li>。
我们再换个电影验证下找的规律是否正确。
check后，我们再看一共10页，每页的url有什么相关呢？
第1页：https://movie.douban.com/top250?start=0&filter=
第3页：https://movie.douban.com/top250?start=50&filter=
第7页：https://movie.douban.com/top250?start=150&filter=
发现只有start后面是有变化哒，规律就是第N页，start=(N-1)*25
基于以上分析，我们有两种写爬虫的思路。
思路一：先爬取最小共同父级标签 <li>，然后针对每一个父级标签，提取里面的序号/电影名/评分/推荐语/链接。
思路二：分别提取所有的序号/所有的电影名/所有的评分/所有的推荐语/所有的链接，然后再按顺序一一对应起来。
"""
"""
import requests, random, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']

        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)



"""
import requests, bs4

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(x * 25)
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    m_list = soup.select("#content .article .grid_view>li")
    for titles in m_list:
        num = titles.find('em', class_="").text
        # 查找序号
        title = titles.find('span', class_="title").text
        # 查找电影名
        tes = titles.find('span', class_="inq").text
        # 查找推荐语
        comment = titles.find('span', class_="rating_num").text
        # 查找评分
        url_movie = titles.find('a')['href']
        
        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)

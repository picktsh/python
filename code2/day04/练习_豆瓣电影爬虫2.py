"""
第四步：书写思路二代码

分别提取所有的序号/所有的电影名/所有的评分/所有的推荐语/所有的链接，然后再按顺序一一对应起来。
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

# 这里偷个懒,因为按思路二提取,这样一一对应的耦合性非常高,不建议使用

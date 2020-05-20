"""
1.题目要求
项目目标：使用多协程和队列，爬取时光网电视剧TOP100的数据（剧名、导演、主演和简介），并用csv模块将数据存储下来。
时光网TOP100链接：http://www.mtime.com/top/tv/top100/
"""
"""
#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。
"""

import queue
import gevent
import requests
import bs4

# 先处理需要请求的链接
url_list = ["http://www.mtime.com/top/tv/top100/"]
for i in range(9):
    url = "http://www.mtime.com/top/tv/top100/index-{}.html".format(i + 2)
    url_list.append(url)


# print(url_list)  # 拼接需要发起请求的所有链接

# 优化错误处理
def _try(fn):
    try:
        return fn()
    except AttributeError:
        print("发生了一个AttributeError错误,但是无关紧要")
        return ""
    except Exception:
        return ""


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
for url in url_list:
    print("发起请求:", url)
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        # print(r.content)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        # print(soup)
        soup_movies = soup.select("#asyncRatingRegion>li")
        # print(soup_movies)  # 当前页面所有的电影<li>
        movie_list = []
        movie = {}
        for m in soup_movies:
            # print(m)
            movie["剧名"] = _try(lambda: m.select_one(".mov_con .px14.pb6 a").text)
            movie["导演"] = _try(lambda: m.select(".mov_con p a")[0].text)
            movie["主演"] = _try(lambda: m.select(".mov_con p a")[1].text)
            movie["简介"] = _try(lambda: m.select_one(".mov_con p.mt3").text)
            movie["评分"] = _try(lambda: m.select_one(".mov_point .point").text)
            print(movie)
            movie_list.append(movie)

print("程序结束-但练习并没有做全")

# 本步骤不需要模拟登录
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/
"""
二、获取书籍id

想要请求推荐XHR，我们需要拿到参数id，也就是书籍id

小说排行榜：https://www.xslou.com/top/allvisit_1/

提示1：
本步骤不需要模拟登录
网站的编码模式是gbk
"""
# 本步骤不需要模拟登录
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/

# 爬取链接html页面中a标签的链接以及内容
import requests
from bs4 import BeautifulSoup

url = 'https://www.xslou.com/top/allvisit_1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
results = requests.get(url, headers=headers)
# print(results.status_code)
if results.status_code == 200:
    results.encoding = 'gbk'
    # print(results.text)
    bs = BeautifulSoup(results.text, 'html.parser')
    # print(bs)
    ols = bs.select('ul.update')  # [ul,ul,ul]
    # print(ols)
    if len(ols) == 0:
        print('空列表:', ols)
    for ls in ols:
        href = ls.find('a')['href']  # 其中有多个链接,我们只拿第一个
        # url_text = ls.find('a').text
        print(href)  # https://www.xslou.com/yuedu/9356/
        # 分割最后位置的数字,拿到book_id
        book_id = href.split('/')[-2]
        print(book_id)  # 9356

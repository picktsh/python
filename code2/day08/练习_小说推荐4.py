# 小说楼：https://www.xslou.com/
# 小说楼登录：https://www.xslou.com/login.php
# 小说楼的排行榜：https://www.xslou.com/top/allvisit_1/
# 小说楼推荐：https://www.xslou.com/modules/article/uservote.php?id=

import requests
from bs4 import BeautifulSoup

login_url = 'https://www.xslou.com/login.php'
hot_url = 'https://www.xslou.com/top/allvisit_1/'
urge_url = 'https://www.xslou.com/modules/article/uservote.php?id='
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


def login_cookies():
    data = {
        'username': input('请输入你的账号:'),
        'password': input('请输入你的密码:'),
        'action': 'login'
    }
    result = session.post(login_url, headers=headers, data=data)
    # 请求是否成功? 反馈原因
    # 解析内容,判断用户是否登陆成功? 重新登陆/退出


def get_bookids():
    result = requests.get(hot_url, headers=headers)
    result.encoding = 'gbk'
    bs = BeautifulSoup(result.text, 'html.parser')
    uls = bs.find_all('span', class_='up2')
    books = {}
    for li in uls:
        book_name = li.find('a').text
        link = li.find('a')['href']
        id_list = list(filter(str.isdigit, link))
        book_id = ''.join(id_list)
        books[book_id] = book_name
    return books


def urge(book_id):
    url = urge_url + book_id
    result = session.get(url, headers=headers, cookies=session.cookies)
    # 请求是否成功?
    # 用户是否登陆?
    result.encoding = 'gbk'
    if result.status_code == 200:
        bs = BeautifulSoup(result.text, 'html.parser')
        urge_info = bs.find('div', class_='blocktitle').get_text()
        urge_info2 = bs.find('div', class_='blockcontent').get_text()
        print(urge_info)
        print(urge_info2)


def main():
    login_cookies()
    books = get_bookids()
    print('--------热门书籍--------')
    for k, v in books.items():
        print(k, ':', v)
    book_id = input('请输入想要推荐的书籍id：')
    # 用户出入的 book_id 是否符合要求? 必须是books中存在的,否则重新输入
    # 类型必须是 str
    urge(book_id)


main()

"""
三、带cookies和参数请求推荐链接

将上述两组代码组合。

拿到cookies和参数，完成推荐请求（不要超过5次）

我帮你预置了前两个代码，你可以在此基础上完成本关卡任务。

注意：

请求url需要拼接书籍id
请求时候别忘了添加请求头和cookies:cookies=session.cookies
"""

# 将上述两组代码组合。拿到cookies和参数，完成推荐请求。
# 我帮你预置了前两个代码，你可以在此基础上完成本关卡任务。

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
cookie = ''


def login_cookies():
    global cookie
    data = {
        'username': input('请输入你的账号:'),
        'password': input('请输入你的密码:'),
        'action': 'login'
    }
    result = session.post(login_url, headers=headers, data=data)
    if result.status_code == 200:
        print('请求成功! 账号对不对就不知道咯')
        cookie = result.cookies
    else:
        print('登陆失败!', login_url)


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
    return books  # {'9356':'纯阳武神'}


def urge(book_id):
    print('您选择了:', book_id)
    # 带cookie请求
    # 处理返回结果
    # 给用户提示


# 请求推荐链接需要拼接book_id
# 请求需要带上headers和cookies

def main():
    login_cookies()
    books = get_bookids()
    print('--------热门书籍--------')
    for k, v in books.items():
        print(k, ':', v)
    book_id = input('请输入想要推荐的书籍id：')
    urge(book_id)


if __name__ == '__main__':
    main()
    print('程序结束')

"""
存储cookies
我们先把登录的cookies打印出来看看，请点击运行下面的代码（账号：spiderman;密码：crawler334566）
"""
import requests

session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log': input('请输入账号：'),
    'pwd': input('请输入密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
session.post(url, headers=headers, data=data)
print(type(session.cookies))
# 打印cookies的类型,session.cookies就是登录的cookies
print(session.cookies)
# 打印cookies

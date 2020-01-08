"""
post请求
"""
import requests

# 引入requests。
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 把登录的网址赋值给url。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
data = {
    'log': 'spiderman',  # 写入账户
    'pwd': 'crawler334566',  # 写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
    'testcookie': '1'
}
# 把有关登录的参数封装成字典，赋值给data。
login_in = requests.post(url, headers=headers, data=data)
# 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
print(login_in)
# 打印login_in

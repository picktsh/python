"""
我会先带你写一遍发表评论的代码（要认真看注释）：
"""
import requests

# 引入requests。
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 把请求登录的网址赋值给url。
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
cookies = login_in.cookies
# 提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 我们想要评论的文章网址。
data_1 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# 把有关评论的参数封装成字典。
comment = requests.post(url_1, headers=headers, data=data_1, cookies=cookies)
# 用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
# 调用cookies的方法就是在post请求中传入cookies=cookies的参数。
print(comment.status_code)
# 打印出comment的状态码，若状态码等于200，则证明我们评论成功。

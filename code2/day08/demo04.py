"""
使用 session 优化后的发表评论的代码如下（重点看有注释的代码）：
"""
import requests

# 引用requests。
session = requests.session()
# 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log': input('请输入账号：'),  # 用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去。
    'pwd': input('请输入密码：'),
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
session.post(url, headers=headers, data=data)
# 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数。

url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 把我们想要评论的文章网址赋值给url_1。
data_1 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# 把有关评论的参数封装成字典。
comment = session.post(url_1, headers=headers, data=data_1)
# 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment)
# 打印comment

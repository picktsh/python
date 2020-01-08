import requests

# 登陆的请求地址
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# 登陆的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 登陆的请求参数
data = {
    'log': 'spiderman',  # 写入账户
    'pwd': 'crawler334566',  # 写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-admin/',
    'testcookie': '1'
}
login_in = requests.post(url, headers=headers, data=data)
# ???如果请求成功,但是密码错误了,status_code 也是200,这里需要看页面返回什么内容,进行判定才知道是否登陆成功
# 登陆成功后的
cookies = login_in.cookies
print(cookies)
print(login_in.text)
# 发表文章的请求地址
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_1 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '13',
    'comment_parent': '0'
}
comment = requests.post(url_1, headers=headers, data=data_1, cookies=cookies)
print(comment.status_code)

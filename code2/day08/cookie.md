## cookie 带着小饼干登陆

### 1. 发表博客评论

 - post请求

```python
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
```
使用 session 做请求
```python
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
```
RequestsCookieJar是cookies对象的类，cookies本身的内容有点像一个列表，里面又有点像字典的键与值，具体的值我们看不懂，也不需要弄懂。

那怎么把cookies存储下来？能不能用文件读写的方式，把cookies存储成txt文件？

可是txt文件存储的是字符串，刚刚打印出来的cookies并不是字符串。那有没有能把cookies转成字符串的方法？

对了，在第4关我们知道，json模块能把字典转成字符串。我们或许可以先把cookies转成字典，然后再通过json模块转成字符串。这样，就能用open函数把cookies存储成txt文件。


> 最后，还想和你多说几句——

其实，计算机之所以需要cookies和session，是因为HTTP协议是无状态的协议。

何为无状态？就是一旦浏览器和服务器之间的请求和响应完毕后，两者会立马断开连接，也就是恢复成无状态。

这样会导致：服务器永远无法辨认，也记不住用户的信息，像一条只有7秒记忆的金鱼。是cookies和session的出现，才破除了web发展史上的这个难题。

cookies不仅仅能实现自动登录，因为它本身携带了session的编码信息，网站还能根据cookies，记录你的浏览足迹，从而知道你的偏好，只要再加以推荐算法，就可以实现给你推送定制化的内容。

比如，淘宝会根据你搜索和浏览商品的记录，给你推送符合你偏好的商品，增加你的购买率。cookies和session在这其中起到的作用，可谓举足轻重。

### 2. cookies及其用法
### 3. session及其用法
### 4. 储存cookies
### 5. 读取cookies











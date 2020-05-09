"""
代码实现：
1.登录博客人人都是蜘蛛侠。
2.在文章《未来已来（三）——同九义何汝秀》中，发表一个评论，这个评论中必须要带有“selenium”这个词。
博客登录页面:
https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php
答这道题的时候，使用可视模式会对运行结果有更直观的了解，如果你想看到浏览器的操作过程，建议你在本地写好练习答案，然后再复制到这里。
想不出怎么做？点击步骤旁边的问号查看提示。
"""
# 本地Chrome浏览器设置方法
from selenium import webdriver  # 从selenium库中调用webdriver模块
import time  # 调用time模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
print("程序开始...")
driver.get("https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php")
print("请求完成")
time.sleep(1)


# 登录的方法
def userLogin():
    username = input("请输入用户名或电子邮件地址:")
    password = input('请输入密码：')  # 想办法下隐藏用户输入的密码

    driver.find_element_by_id("user_login").send_keys(username)
    driver.find_element_by_id("user_pass").send_keys(password)
    print("点击登录前...")
    driver.find_element_by_id("wp-submit").click()
    time.sleep(1)
    try:
        driver.find_element_by_class_name("site-content-contain")
        print("登录成功")
    except BaseException:
        print("账号或密码输错误! 请再试一次")
        userLogin()


# 发表评论
def addComment():
    # 找到输入框,输入内容,点击发送

    commentContent = time.asctime() + "  Author: rise 爬虫第9节,练习要求这个评论中必须要带有“selenium”这个词。"
    print("您的评论内容:" + commentContent)
    driver.find_element_by_id("comment").send_keys(commentContent)
    print("发表评论")
    driver.find_element_by_id("submit").click()
    print("发表评论完成")


# 登录
userLogin()
time.sleep(1)

# 进入文章
driver.find_element_by_id("post-20").find_element_by_tag_name("a").click()
print("进入文章")
time.sleep(1)

# 发表评论
addComment()

# 查找文章和发表评论
time.sleep(3)
print("程序结束")
driver.close()

# 本地Chrome浏览器设置方法
from selenium import webdriver  # 从selenium库中调用webdriver模块
import time  # 调用time模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器

# 教学系统设置浏览器的方法
# from selenium.webdriver.chrome.webdriver import RemoteWebDriver  # 从selenium库中调用RemoteWebDriver模块
# from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
# import time
#
# chrome_options = Options()  # 实例化Option对象
# chrome_options.add_argument('--headless')  # 对浏览器的设置
# # 声明浏览器对象
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities())

driver.get("https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html")
time.sleep(2)

driver.find_element_by_class_name("js_get_more_hot").click()
time.sleep(1)

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')  # 使用class_name找到评论
for comment in comments:  # 循环
    sweet = comment.find_element_by_tag_name('p')  # 找到评论
    print('评论：%s\n ---\n' % sweet.text)  # 打印评论

print(len(comments))  # 打印获取到的评论个数

driver.close()  # 关闭浏览器

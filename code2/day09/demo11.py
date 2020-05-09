# 教学系统的浏览器设置方法
from selenium.webdriver.chrome.webdriver import RemoteWebDriver  # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
from bs4 import BeautifulSoup
import time

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 对浏览器的设置
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub",
                         chrome_options.to_capabilities())  # 声明浏览器对象

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')  # 访问页面
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot')  # 根据类名找到【点击加载更多】
button.click()  # 点击
time.sleep(2)  # 等待两秒

pageSource = driver.page_source  # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource, 'html.parser')  # 使用bs解析网页
comments = soup.find('ul', class_='js_hot_list').find_all('li', class_='js_cmt_li')  # 使用bs提取元素
print(len(comments))  # 打印comments的数量

for comment in comments:  # 循环
    sweet = comment.find('p')  # 提取评论
    print('评论：%s\n ---\n' % sweet.text)  # 打印评论
driver.close()  # 关闭浏览器

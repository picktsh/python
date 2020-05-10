from bs4 import BeautifulSoup
import time

# 本地Chrome浏览器的静默默模式设置：
from selenium import webdriver  # 从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行

driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
print("页面请求成功")
time.sleep(1)

print("点击提交按钮,进入禅页面")
driver.find_element_by_css_selector("#div2 .sub").click()
time.sleep(1)

pageSource = driver.page_source
soup = BeautifulSoup(pageSource, "html.parser")
# print(soup)
contents = soup.find_all(class_="content")
for c in contents:
    print(type(c))
    print(c.find(id="p").text)

time.sleep(2)
driver.close()
print("浏览器关闭")

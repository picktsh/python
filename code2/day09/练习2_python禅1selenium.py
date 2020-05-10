"""
题目要求
获取网站你好，蜘蛛侠！的Python之禅中文英对照文本。
需要通过两种方法获取：
只使用selenium
selenium与BeautifulSoup配合
"""
"""
第一种方法：selenium
这次我们要用selenium单独完成这个爬虫。
获取数据、解析数据、提取数据这三个步骤全部都由selenium来完成。
写代码吧~
想不出怎么做？点击步骤旁边的问号查看提示。
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
print("页面请求成功")
time.sleep(2)

print("点击提交按钮,进入禅页面")
driver.find_element_by_css_selector("#div2 .sub").click()
time.sleep(1)

# 获取英文和中文-并输出
contents = driver.find_elements_by_css_selector(".content")
for c in contents:
    print(c.find_element_by_id("p").text)

time.sleep(2)
driver.close()
print("浏览器关闭")

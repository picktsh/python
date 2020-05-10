from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

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

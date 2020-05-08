# 本地Chrome浏览器设置方法
from selenium import webdriver
import time

driver = webdriver.Chrome()
# 教学系统的浏览器设置方法
# from selenium.webdriver.chrome.webdriver import RemoteWebDriver # 从selenium库中调用RemoteWebDriver模块
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
# import time
#
# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 对浏览器的设置
# driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 声明浏览器对象

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

pageSource = driver.page_source  # 获取完整渲染的网页源代码
print(type(pageSource))
print(pageSource)
driver.close()

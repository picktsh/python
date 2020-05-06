# 教学系统的浏览器设置方法，你不需要记住它
from selenium.webdriver.chrome.webdriver import RemoteWebDriver  # 从selenium库中调用RemoteWebDriver模块
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类

chrome_options = Options()  # 实例化Option对象
chrome_options.add_argument('--headless')  # 对浏览器的设置
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub",
                         chrome_options.to_capabilities())  # 设置浏览器引擎

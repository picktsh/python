# 本地Chrome浏览器设置方法
from selenium import webdriver  # 从selenium库中调用webdriver模块
import time  # 调用time模块

driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')  # 访问页面
time.sleep(2)  # 暂停两秒，等待浏览器缓冲

teacher = driver.find_element_by_id('teacher')  # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀')  # 输入文字
assistant = driver.find_element_by_name('assistant')  # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢')  # 输入文字
time.sleep(1)
button = driver.find_element_by_class_name('sub')  # 找到【提交】按钮
time.sleep(1)
button.click()  # 点击【提交】按钮
time.sleep(1)
driver.close()  # 关闭浏览器


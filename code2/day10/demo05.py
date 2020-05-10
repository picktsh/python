import schedule
import time


# 引入schedule和time模块
def job():
    print("I'm working...")


# 定义一个叫job的函数，函数的功能是打印'I'm working...'
schedule.every(2).seconds.do(job)  # 每2s执行一次job()函数

while True:
    schedule.run_pending()
    time.sleep(1)

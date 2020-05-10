import schedule
import time


# 引入schedule和time

def job():
    print("I'm working...")


# 定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule.every(10).minutes.do(job)  # 部署每10分钟执行一次job()函数的任务
schedule.every().hour.do(job)  # 部署每×小时执行一次job()函数的任务
schedule.every().day.at("10:30").do(job)  # 部署在每天的10:30执行job()函数的任务
schedule.every().monday.do(job)  # 部署每个星期一执行job()函数的任务
schedule.every().wednesday.at("13:15").do(job)  # 部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)
    # 15-17都是检查部署的情况，如果任务准备就绪，就开始执行任务。

"""怎么让程序只执行N次"""

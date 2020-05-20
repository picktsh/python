from gevent import monkey

# 从gevent库里导入monkey模块。
monkey.patch_all()
# monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent, time, requests

# 导入gevent、time、requests。

start = time.time()
# 记录程序开始时间。

url_list = ['https://www.baidu.com/',
            'https://www.sina.com.cn/',
            'http://www.sohu.com/',
            'https://www.qq.com/',
            'https://www.163.com/',
            'http://www.iqiyi.com/',
            'https://www.tmall.com/',
            'http://www.ifeng.com/']


# 把8个网站封装成列表。

def crawler(url):
    # 定义一个crawler()函数。
    r = requests.get(url)
    # 用requests.get()函数爬取网站。
    print(url, time.time() - start, r.status_code)


# 打印网址、请求运行时间、状态码。

tasks_list = []
# 创建空的任务列表。

for url in url_list:
    # 遍历url_list。
    task = gevent.spawn(crawler, url)
    # 用gevent.spawn()函数创建任务。
    tasks_list.append(task)
# 往任务列表添加任务。
gevent.joinall(tasks_list)
# 执行任务列表里的所有任务，就是让爬虫开始爬取网站。
end = time.time()
# 记录程序结束时间。
print(end - start)
# 打印程序最终所需时间。

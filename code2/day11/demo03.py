# queue模块
from gevent import monkey

monkey.patch_all()
import gevent, time, requests
from gevent.queue import Queue

start = time.time()

url_list = ['https://www.baidu.com/',
            'https://www.sina.com.cn/',
            'http://www.sohu.com/',
            'https://www.qq.com/',
            'https://www.163.com/',
            'http://www.iqiyi.com/',
            'https://www.tmall.com/',
            'http://www.ifeng.com/']

work = Queue()
for url in url_list:
    work.put_nowait(url)


def crawler():
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url)
        print(url, work.qsize(), r.status_code)


tasks_list = []

for x in range(2):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)

end = time.time()
print(end - start)

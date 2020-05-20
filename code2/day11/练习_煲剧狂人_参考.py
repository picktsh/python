from gevent import monkey

monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

work = Queue()
url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)

url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(1, 11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)


def crawler():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url, headers=headers)
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        datas = bs_res.find_all('div', class_="mov_con")
        for data in datas:
            TV_title = data.find('a').text
            data = data.find_all('p')
            TV_data = ''
            for i in data:
                TV_data = TV_data + '' + i.text
            writer.writerow([TV_title, TV_data])
            print([TV_title, TV_data])


csv_file = open('timetop.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)

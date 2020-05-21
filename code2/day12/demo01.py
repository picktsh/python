"""
代码要求：导入所需模块，并根据前面分析得出的网址规律，用for循环构造出前3个常见食物类别的前3页食物记录的网址和第11个常见食物类别的前3页食物记录的网址，并把这些网址放进队列，打印出来。
"""
# 导入所需的库和模块：
from gevent import monkey

monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

work = Queue()
# 创建队列对象，并赋值给work。

# 前3个常见食物分类的前3页的食物记录的网址：
url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)
# 通过两个for循环，能设置分类的数字和页数的数字。
# 然后，把构造好的网址用put_nowait方法添加进队列里。

# 第11个常见食物分类的前3页的食物记录的网址：
url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
for x in range(1, 4):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)
# 通过for循环，能设置第11个常见食物分类的食物的页数。
# 然后，把构造好的网址用put_nowait方法添加进队列里。

print(work)
# 打印队列

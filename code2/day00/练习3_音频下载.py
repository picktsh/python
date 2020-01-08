import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

with open(r'test.mp3', 'ab') as file:  # 保存到本地的文件名
    file.write(res.content)
    file.flush()
"""
概述
flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
"""

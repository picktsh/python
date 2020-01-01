import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

with open(r'test.mp3', 'ab') as file:  # 保存到本地的文件名
    file.write(res.content)
    file.flush()

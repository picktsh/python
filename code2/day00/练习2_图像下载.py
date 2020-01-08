import requests

url = 'https://res.pandateacher.com/2019-01-12-15-29-33.png'
res = requests.get(url)

with open('test.png', 'wb+') as f:
    # 图片类型,使用二进制的形式写入
    f.write(res.content)

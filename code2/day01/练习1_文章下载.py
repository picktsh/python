import requests

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md'
res = requests.get(url)

with open('test.txt', 'w+', encoding='utf-8') as f:
    f.write(res.text)

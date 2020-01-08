"""
课堂练习
获取这个书苑不太冷的网页源代码，并且保存文件到本地。

URL：https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html

忘记怎么写了？点击下面的"需要帮助"。
"""
import requests

url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html'

res = requests.get(url)

with open(r'demo02.html', 'w+', encoding='utf-8') as f:
    f.write(res.text)
    f.flush()

print('程序结束')

"""
参考代码
"""
# 调用requests模块
import requests

# 获取网页源代码，得到的res是response对象。
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 检测请求是否正确响应
print(res.status_code)

# 正确响应，进行读写操作
# 新建一个名为book的html文档，你看到这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 字符串需要以w读写。你在学习open()函数时接触过它。
if res.status_code == 200:
    file = open('book.html', 'w')
    # res.text是字符串格式，把它写入文件内。
    file.write(res.text)
    # 关闭文件
    file.close()

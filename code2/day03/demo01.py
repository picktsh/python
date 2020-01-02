"""
最后，还写了这样一段代码：即通过调用requests库，获取到了网页源代码，并将它写入到本地：
"""
# 调用requests模块
import requests

# 获取网页源代码，得到的res是response对象。
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 检测请求是否正确响应
print(res.status_code)

# 新建一个名为book的html文档，你看到这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 字符串需要以w读写。你在学习open()函数时接触过它。
file = open('book.html', 'w')
# res.text是字符串格式，把它写入文件内。
file.write(res.text)
# 关闭文件
file.close()

"""
【练习时间】请你把上面csv文件写入的代码敲一遍。毕竟代码是绝对不能光看不敲的，快，敲起来！提示：先引入csv模块，用open()函数打开csv文件，不要忘了加newline=' '参数；然后利用csv.writer()函数创建一个writer对象，再调用writerow()方法，就可以往csv文件里写入内容。
"""
import csv

csv_file = open('demo.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(csv_file)
write.writerow(['电影', '豆瓣评分'])
rows = [['银河护卫队', '8.0'], ['复仇者联盟', '8.1'], ['中国机长', '9.4']]
for i in rows:
    write.writerow(i)
csv_file.close()

"""
用csv模块写入数据这一个知识点我们已经清楚。接下来我们可以继续学习怎么读取csv文件的数据。

以刚刚创 建好的“demo.csv”文件为例。你可以先运行下面的代码，看看会读取出什么结果。
"""
import csv

csv_file = open('demo.csv', 'r', newline='', encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)
csv_file.close()

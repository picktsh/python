"""
方案3: 将邮箱地址写入csv模块的方法是write();
步骤是：
1.引入csv模块；
2.提供需要写入csv文件的数据，
3.建文件并写入。
"""
# 创建一个邮件地址的文件
import csv

# 引用csv模块。

data = [['wufeng ', 'wufeng@qq.com'], ['kaxi', 'kaxi@qq.com']]
# 待写入csv文件的内容

with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

"""
读取的过程就异曲同工了。利用的是read()方法。
步骤是：
1.引入csv模块；
2.打开csv文件；
3.读取需要的数据。
"""
# 引用csv模块。(在前面已经引入了)

with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        to_addrs = row[1]

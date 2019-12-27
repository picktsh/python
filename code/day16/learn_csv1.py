import csv

with open("test1.csv", newline='')  as f:
    reader = csv.reader(f)
    # 使用csv的reader()方法，创建一个reader对象
    for row in reader:
        # 遍历reader对象的每一行
        print(row)

print("读取完毕！")

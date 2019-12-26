# 打开文件
file1 = open(file='/Users/Ted/Desktop/test/abc.txt', mode='r', encoding='utf-8')
# 读文件
filecontent = file1.read()
# 显示内容
print(filecontent)
# 关闭文件
file1.close()

# 为了避免打开文件后忘记关闭，占用资源或当不能确定关闭文件的恰当时机的时候，我们可以用到关键字with，之前的例子可以写成这样：
# 普通写法
file1 = open('abc.txt', 'a')
file1.write('张无忌')
file1.close()

# 使用with关键字的写法
with open('abc.txt', 'a') as file1:
    # with open('文件地址','读写模式') as 变量名:
    # 格式：冒号不能丢
    file1.write('张无忌')
    # 格式：对文件的操作要缩进
    # 格式：无需用close()关闭

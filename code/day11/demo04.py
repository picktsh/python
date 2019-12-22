# bug 4：被动掉坑
# 我们举个例子，当运行以下代码的时候，如果输入的东西不是数字，则程序一定会报错。
'''
age = int(input('你今年几岁了？'))
if age < 18:
    print('不可以喝酒噢')
'''

# 提示：需要用到try……except……语句，以及while语句和break语句。

try:
    age = int(input('你今年几岁了？'))
    if age < 18:
        print('不可以喝酒噢')
except ValueError:
    print('要输入整数噢')

# 参考答案
# 不用修改代码，直接运行即可，尝试多输入几次非数字
while True:
    try:
        age = int(input('你今年几岁了？'))
        break
    except ValueError:
        print('你输入的不是数字！')

if age < 18:
    print('不可以喝酒噢')
# 代码要点有两个：
# （1）因为不知道用户什么时候才会输入正确，所以设置while循环来接受输入，只要用户输入不是数字就会一直循环，输入了数字就break跳出循环。
# （2）使用try……except……语句，当用户输错的时候会给予提示。

# 我们再来看一个例子，下列代码的目的是遍历列表中的数字，依次用6除以他们。你可以运行一下，看看报错类型是什么，然后点击跳过本题。
'''
num = [1, 2, 0, 3]
for x in num:
    print(6 / x)
'''
'''
Traceback (most recent call last):
  File "/home/python-class/classroom/apps-1-id-5cd9765e19bbcf00015547b8/140/main.py", line 3, in <module>
    print (6/x)
ZeroDivisionError: division by zero
'''
# 这时呢，你可以使用try…except语句来帮助你：如果出现ZeroDivisionError就提醒'0不能做除数'，现在请你尝试把代码补全吧～

num = [1, 2, 0, 3]
for x in num:
    try:
        print(6 / x)
    except:
        print('0 不能作为 被除数计算')

# 参考代码
num = [1, 2, 0, 3]
for x in num:
    try:
        # 尝试执行下列代码
        print(6 / x)
    # 使用6除以num中的元素，并打印
    except ZeroDivisionError:
        # 除非发生ZeroDivisionError报错，执行下列代码：
        print('0是不能做除数的！')  # 打印“0是不能做除数的！”

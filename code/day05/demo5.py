# 此关卡如果遇到 死循环,按3次 Ctrl + C 强制退出
# 此关卡如果遇到 死循环,按3次 Ctrl + C 强制退出
# 此关卡如果遇到 死循环,按3次 Ctrl + C 强制退出

# for...in...循环语句

for i in [1, 2, 3, 4, 5]:
    print(i)

# 有一群数字在排队办业务，也就是列表[1,2,3,4,5]
# 它们中的每一个被叫到号的时候(for i in)，就轮流进去一个空房间办业务
# 每一个数字进去房间之后，都对计算机说：“喂，我要办这个业务：帮忙把我自己打印出来”，也就是print(i)
# 然后计算机忠实的为每一个数字提供了打印服务，将1,2,3,4,5都打印在了屏幕上

dict = {'日本': '东京', '英国': '伦敦', '法国': '巴黎'}

for i in dict:
    print(i)
# 不要怀疑，字符串也属于“一群排队办业务的人”。打个比方，'吴承恩'三个字就像一家三口，但走进空房间办业务时，这家人是可以一个一个进去的。来试试吧。
# 而整数、浮点数是不属于“一群排队办业务的人”的，如果把它们放在for循环里，代码会报错。

# range()函数 值域 范围 极差
# 请直接运行代码
for i in range(3):
    print(i)
for i in range(13, 17):
    print(i)
# 使用range(a,b) 函数，你可以生成了一个【取头不取尾】的整数序列。

# 重要的事情说三遍，哈哈。像这样，有了range()函数之后，当你想把一段代码固定重复n次时，就可以直接使用for i in range(n)解决问题。
# 来练习一下：如果你要重复打印“书桓走的第n天，想他”，n为0到10，你会怎么写？
for i in range(11):
    print('书恒走的第' + str(i) + '天，想他')

# range()函数还有一种用法，我们来直接运行体验一下：
for i in range(0, 10, 3):
    print(i)
# 用for循环完成1-100分别乘以5的计算
for i in range(1, 101):
    print(str(i * 5))

# 请你来动手用for循环代替以上重复性代码，并起到同样的效果。
d = {'小明': '醋', '小红': '油', '小白': '盐', '小张': '米'}
for i in d:
    print(d[i])

# while循环

a = 0  # 先定义变量a，并赋值
while a < 5:  # 设定一个放行条件：a要小于5，才能办事
    a = a + 1  # 满足条件时，就办事：将a+1
    print(a)  # 继续办事：将a+1的结果打印出来

man = ''  # 注：''代表空字符串
while man != '有':  # 注：!=代表不等于
    man = input('有没有愿意为小龙女死的男人？没有的话就不能出古墓。(有)')
print('小龙女可以出古墓门下山啦~')

password = ''  # 变量password用来保存输入的密码
while password != '816':
    password = input('请尝试输入密码(816)：')
print('欢迎回家!')

a = 0  # 定义了一个变量a
# 有缩进的时候，print(a); 也是循环中的“办事流程”，会将数字逐一打印。没有缩进的时候，循环中的“办事流程”就只有做加法，print(a); 也就只会打印循环结束时的最后一个数字。
while a < 5:  # 当a小于5的时候，就自动执行后续缩进部分的语句
    print('现在a的值是：' + str(a))  # 加一个print看看现在的a是多少
    a = a + 1  # 每执行一次循环，变量a的值都加1
    print('加1后a的值是：' + str(a))  # 加一个print看看加1后的a是多少
print(a)

for i in range(1, 101):
    print(i * 5)
# 如果现在用while循环，应该怎么写呢？你来试试看。
a = 1
while a < 101:
    print(a * 5)
    a += 1
# 所以说，当我们【工作量确定】的时候，我们就可以让for循环来完成重复性工作。反之，要【工作量不确定时】可以让while循环来工作：
# 适合用for...in...循环
for i in '神雕侠侣':
    print(i)

# 适合用while循环
password = ''
while password != '816':
    password = input('请尝试输入密码：')

# 不过有一种情况for循环和while循环都可以解决问题，那就是【把一件事情做N遍】：
# 用for循环把诗句打印3遍
for i in range(1, 4):
    print('明日复明日，明日何其多。')

# 用while循环把诗句打印3遍
j = 1
while j < 4:
    print('明日何其多，明日何其多。')
    j = j + 1

# =======================练习=====================
# 请你用for循环完成小美的愿望。
# 小美想知道你是怎么用 for循环 的，在下方写下你的代码吧~
for i in range(1, 8):
    if i != 4:
        print(i)
# 小美还想知道你是怎么用 while循环 的，在下方写下你的代码吧~
i = 1
while i <= 7:
    if i != 4:
        print(i)
    i += 1

# 查看注释，运行代码。

# while 循环
n = 0
while n < 7:
    n = n + 1
    if n != 4:  # 当num != 4，执行打印语句；等于4时不打印。
        print(n)

# for 循环
for num in range(1, 8):  # 为同时能运行两个循环，新取参数 num。
    if num != 4:  # 当num != 4，执行打印语句；等于4时不打印。
        print(num)

# =======================练习2=====================
# 练习目标
# 通过这个练习，你会尝试用循环来解决生活中的问题，并了解一种新的列表方法。
#
# 练习要求
# 小明、小红、小刚是同班同学，且坐在同一排，分别坐在第一位、第二位、第三位。
# 由于他们的身高都差不多，所以，老师计划让他们三个轮流坐在第一位。
# 每次换座位的时候，第一位变第三位，后面两位都往前一位

# 方法1：append()函数
# 可结合循环和append()函数，让列表发生3次变化，每次都打印出来，如下：
students = ['小明', '小红', '小刚']
for i in range(3):
    current = students[0]
    del students[0]
    students.append(current)
    print(students)

# 参考代码
students = ['小明', '小红', '小刚']
for i in range(3):
    student1 = students[0]  # 获取第一个座位的学生 student1
    students = students[1:]  # 让 student1 暂时离开，后面的学生座位都进一位。
    students.append(student1)  # 将 student1 安排到最后一个座位
    print(students)

# 方法2：pop()函数
# 我们先介绍一下列表中的pop()函数，用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# 可以将其理解为提取和删除的融合：①提取：取到元素，对列表没有影响；②删除：删除列表的元素。
# 而移除，则是同时做到取到元素，并且删除列表中的元素。
print('提取只取不删：')
list1 = ['0', '1', '2', '3']
print(list1[3])
print(list1)

print('\n删除(del)只删不取：')
list1 = ['0', '1', '2', '3']
del list1[3]
print(list1)

print('\n移除（pop）又取又删：')
list1 = ['0', '1', '2', '3']
print(list1.pop())  # 默认删除最后一个元素，并返回该元素的值。
print(list1)
print(list1.pop(0))  # 也可指定删除某个元素，并返回该元素的值。
print(list1)

students = ['小明', '小红', '小刚']
for i in range(3):
    student1 = students.pop(0)  # 运用pop()函数，同时完成提取和删除。
    students.append(student1)  # 将移除的student1安排到最后一个座位。
    print(students)

# 结尾

# 请阅读代码后再直接运行

print('以下数据判断结果都是【假】：')
print(bool(False))
print(bool(0))
print(bool(''))
print(bool(None))

print('以下数据判断结果都是【真】：')
print(bool(True))
print(bool(1))
print(bool('abc'))

# 还是用例子来说明吧。我们先看看【and】和【or】。请先阅读代码，然后直接运行：
# 请先阅读代码，然后直接运行
a = 1
b = -1

print('以下是and运算')
if a == 1 and b == 1:  # 【b实际上是-1】
    print('True')
else:
    print('False')

print('以下是or运算')
if a == 1 or b == 1:  # 【b实际上是-1】
    print('True')
else:
    print('False')

# 你用肉眼就能判断a,b,c三个变量在不在（in或是not in）列表list里面了对吧？来简单运行一个试试呗。
# 直接运行代码即可
list = [1, 2, 3, 4, 5]
a = 1

# 做一次布尔运算，判断“a是否在列表list之中”
print(bool(a in list))
print(bool(a not in list))

# 如果涉及到的数据集合是字典的话，【in】和【not in】就可以用来判断字典中是否存在某个【键】：
# 运行结果会是什么你应该很清楚啦，看看就好~
dict = {'法国': '巴黎', '日本': '东京', '中国': '北京'}
a = '法国'

print(bool(a in dict))

# 今天理解布尔运算原理后，可以把这段代码改造成更“程序员”的方式：
i = 100
while i:
    print('把这句话打印100遍')
    i = i - 1

# 四种新的语句
# 四种新的语句
# 四种新的语句

# break语句
# break语句
# 请运行代码体验效果
for i in range(5):
    print('明日复明日')
    if i == 3:  # 当i等于3的时候触发
        break  # 结束循环

# 下面是一个while循环代码，本来会循环5次，但循环到第3次的时候就被break语句打断，然后结束循环了。
# 请运行代码体验效果
i = 0
while i < 5:
    print('明日复明日')
    i = i + 1
    if i == 3:  # 当i等于3的时候触发
        break  # 结束循环

# 这种年复一年的循环状态，在唐僧师徒来到这里后，结束了。因为孙悟空制服了这个鲤鱼精，百姓再也不用受苦了！真好。
while True:
    print('上供一对童男童女')
    t = input('孙悟空来了吗')
    if t == '来了':
        break
print('孙悟空制服了鲤鱼精，陈家庄再也不用上供童男童女了')

# 我想请你写下这样一个程序，功能是请用户输入密码，如果输入了错误的密码，就一直循环请用户继续输入；如果输入了正确的密码，就结束循环。设定这个密码为'小龙女'。（其实之前做过这题，有印象吗？）
# 提示：① 用while True开启无限循环。② 在循环内部用input() 函数获取用户的数据。 ③ 使用if...break，如果变量p == '小龙女'，那就break结束循环。否则又开始循环。④ 结束循环后，打印--通过啦~
while True:
    pwd = input('功能是请用户输入密码(小龙女):')
    if pwd == '小龙女':
        break
print('程序结束')

# continue语句
# continue语句
# 观察代码，然后运行代码看看是什么结果

# continue语句搭配for循环
for i in range(5):
    print('明日复明日')
    if i == 3:  # 当i等于3的时候触发
        continue  # 回到循环开头
    print('这句话在i等于3的时候打印不出来')

# continue语句搭配while循环
i = 0
while i < 5:
    print('明日复明日')
    i = i + 1
    if i == 3:  # 当i等于3的时候触发
        continue  # 回到循环开头
    print('这句话在i等于3的时候打印不出来')

# 事实上，西夏公主曾和她的意中人虚竹邂逅于一个黑暗的冰窖之中，但两人不知对方姓名，只互称呼“梦姑”和“梦郎”，两人也看不清彼此的脸。因此，西夏公主为了找到虚竹，才进行招亲，并对候选者问出这三个问题。
while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？(黑暗的冰窖)')
    if q1 != '黑暗的冰窖':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？(梦姑)')
    if q2 != '梦姑':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？(不知道)')
    if q3 == '不知道':
        break
print('都答对了，你是虚竹。')

# pass语句
# pass语句

# 请你运行代码体验一下
a = int(input('请输入一个整数:'))
if a >= 100:
    pass  # 如果没有pass来占据一个位置表示“什么都不做”，以上的代码执行起来会报错：（请你先体验一下报错，然后把pass语句加上。)
else:
    print('你输入了一个小于100的数字')

# else语句
# else语句

# 最后一种else语句，我们在条件判断语句见过【else】，其实，else不但可以和if配合使用，它还能跟for循环和while循环配合使用。
for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')

# while else 语法
# 把之前这段for循环的代码改成while循环，要求运行效果相同
i = 0
while i < 5:
    i += 1
    a = int(input('请输入0结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')

# 循环小练习
# 循环小练习 - 猜数字 24
number = 24
cun = 0
while cun < 5:
    cun += 1
    inp = int(input('输入你要猜的数字'))
    if inp > 24:
        print('猜大啦,再来')
        continue
    elif inp < 24:
        print('猜小啦,再来')
        continue
    elif inp == 24:
        print('恭喜你猜对啦;游戏结束')
        break
else:
    print(str(cun) + '次都没猜中,不玩啦')
print('程序结束')

# 老师的答案
secret = 24
for i in range(3):
    guess = input('guess which number is my secret:')
    if int(guess) == secret:
        print('正确！你很棒哦。')  # 输出结果
        break
    elif int(guess) > secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')
else:
    print('给你3次机会都猜不到，你失败了。')



# bug 3：思路不清
# print()函数常和#号注释结合在一起用来debug。下面来讲一个例子：
# 以下是一个同学提交的一段错误代码，大家可以运行看看（记得这里有input()函数，要在终端输入，然后点击enter）：
movie = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '王力宏', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅']
}

name = input('你查询的演员是？')
'''
# 可见这样写取到的全部是字典的键，而非值。这时，就能意识到是这一行出了问题，他可以回看知识点，发现字典的值的取法，然后修改代码。
for i in movie:
    actors = [i]
    if name in actors:
        print(name + '出演了' + i)
'''

for i in movie:
    actors = movie[i]
    if name in actors:
        print(name + '出演了' + i)

# 打铁要趁热，让我们继续来实操。以下代码是一位学员制作的猜硬币游戏，一共有两次猜的机会。
# 猜硬币游戏
import random

guess = ''

while guess not in ['正面', '反面']:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

# 随机抛硬币，0代表正面，1代表反面
toss = random.randint(0, 1)

if ['正面', '反面'][toss] == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，你还有一次机会。')
    guess = input('再输一次“正面”或“反面”：')
    if ['正面', '反面'][toss] == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')

# ########################分割线#####################
# 参考答案
# 第一种方法是先创建一个列表：
# 以下代码无需修改，直接运行即可
import random

all = ['正面', '反面']
guess = ''

while guess not in all:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = input('请输入“正面”或“反面”：')

# 随机抛硬币，0代表正面，1代表反面
toss = all[random.randint(0, 1)]

if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，再给你一次机会。')
    guess = input('再输一次（“正面”或“反面”）：')
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')

# 第二种更为取巧，直接把输入的信息限定为'0'或'1'
# 以下代码无需修改，直接运行即可
import random

guess = ''

while guess not in [0, 1]:
    print('------猜硬币游戏------')
    print('猜一猜硬币是正面还是反面？')
    guess = int(input('“正面”请输入0,“反面”请输入1：'))
    # 注意要用int()将字符串类型转换为数字类型

toss = random.randint(0, 1)

if toss == guess:
    print('猜对了！你真棒')
else:
    print('没猜对，再给你一次机会。')
    guess = int(input('再输一次（“正面”请输入0,“反面”请输入1）：'))
    if toss == guess:
        print('你终于猜对了！')
    else:
        print('大失败！')

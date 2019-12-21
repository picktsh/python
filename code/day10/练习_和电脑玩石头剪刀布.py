# 练习要求：
# 和电脑玩一个剪刀石头布的游戏：电脑随机出拳，我们可选择出什么。
# 首先，我们要让双方选择出拳，才能判断胜负。
# #2 双方出拳
# 我们可以设置变量computer_choice代表电脑的出拳选择，设置变量user_choice代表你的出拳选择。
# 电脑的出拳，我们可以使用random.choice()来随机选择；我们的出拳，可以手动输入我们出拳的类型。
# 另外，判断下输入：当输入的内容不是石头剪刀布时，电脑会提醒'输入有误，请重新出拳'，并重新出拳。
# 请根据已经设置好的代码，补充代码，让代码符合上面的要求。
import random

punches = ['石头', '剪刀', '布']
computer_choice = random.choice(punches)
choice = int(input('请选择出 1:石头,2:剪刀,3:布'))
user_choice = punches[choice]
print(computer_choice, user_choice)

# ##################分割线####################
import random

# #3 双方亮拳
# 你和电脑已经对自己要出的拳进行了选择，接下来，我们需要知道双方的出拳类型。
# 请使用print()函数补充亮拳的结果。

# 出拳
punches = ['石头', '剪刀', '布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑选择: {}'.format(computer_choice))
print('玩家选择: {}'.format(user_choice))


def judge(user, computer):
    if user == computer:
        print('平局!')
    elif (user == '石头' and computer == '剪刀') or (user == '剪刀' and computer == '布') or (
            user == '布' and computer == '石头'):
        print('你赢了！')
    else:
        print('你输了！')


# 胜负
print('—————结果—————')
judge(user=user_choice, computer=computer_choice)

print('程序结束')

# ##################分割线####################
# 参考代码
import random

# 出拳
punches = ['石头', '剪刀', '布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()

# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)

# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
elif (user_choice == '石头' and computer_choice == '剪刀') or (user_choice == '剪刀' and computer_choice == '布') or (
        user_choice == '布' and computer_choice == '石头'):
    print('你赢了！')
else:
    print('你输了！')

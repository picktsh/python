"""
5 参考代码

这次的参考代码，真的是参考代码。你可以将列表中的菜品都换成你喜欢吃的食物。
假如你面对一些做什么选择其实差别不大但还是会纠结的情况，不妨用代码来辅助决策。
可能，看到电脑随机给出的某些决定时，你的心里会冒出“就是它了”或“绝对不要”的想法。
所以，说到底，编程知识和产品思维，是辅助我们工作生活的工具。
好比一个简单的随机选择，可能就让你看清了自己的真实想法。
希望你也能根据自己的需要，为自己定制出一些产品。
"""
# 帮你做选择之我要吃什么
import random

# 将需要用到的表格和变量放在开头
list_food = ['KFC', '蒸菜馆', '楼下快餐店', '桂林米粉', '东北饺子', '金牌猪脚饭', '三及第汤饭']  # 备选菜单，可自定义。
list_choice = []


# 由于两个原因都包含判断过程，所以，为了让代码更简洁，可将其封装成函数。
def choose(list):
    while True:
        food = random.choice(list)
        judgement = input('去吃【%s】好不好啊？同意的话输入y，不想吃直接回车即可。' % (food))
        if judgement == 'y':
            print('去吃【%s】！就这么愉快地决定啦！' % (food))
            break


# 判断环节
reason = int(input('你不知道吃什么的原因是：1.完全不知道吃什么；2.在几家店之间徘徊（请输入1或2）：'))
if reason == 1:
    choose(list_food)
elif reason == 2:
    add = True
    while add:
        choice = input('请输入让你犹豫的店名（注：一家一家输，完成后输入y）：')
        if choice != 'y':  # 这个判断语句，是为了不将 y 也添加到菜单里。
            list_choice.append(choice)
        if choice == 'y':
            add = False
    choose(list_choice)
else:
    print('抱歉，目前还不支持第三种情况——不过，你可以加代码哦。')

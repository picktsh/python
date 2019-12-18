import time
import random

# 后续代码 1秒后再执行
time.sleep(1)

# 调用random模块，与
a = random.randint(1, 100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
print(a)

# 【格式化字符串】
player_life = 120
player_attack = 100
print('血量：' + str(player_life) + ' 攻击：' + str(player_attack))
print('血量：%s 攻击：%s' % (player_life, player_attack))

i = 0
print(' \n——————现在是第' + str(i) + '局——————')  # 替换前
print('  \n——————现在是第 %s 局——————' % i)  # 替换后

print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))  # 替换前
print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))  # 替换后

print('敌人发起了攻击，【玩家】剩余血量' + str(player_life))  # 替换前
print('敌人发起了攻击，【玩家】剩余血量%s' % player_life)  # 替换后

# 进阶练习
# 进阶练习
# 学习format()函数
# format()函数是从 Python2.6 起新增的一种格式化字符串的函数，功能比课堂上提到的方式更强大。
# format()函数用来占位的是大括号{}，不用区分类型码（%+类型码）。
# 具体的语法是：'str.format()'，而不是课堂上提到的'str % ()'。
# 而且，它对后面数据的引用更灵活，不限次数，也可指定对应关系。
# 看完左侧的代码、结果和注释，你就懂上面几句话的意思了。
# % 格式化：str % ()
print('%s%d' % ('数字：', 0))
print('%d，%d' % (0, 1))
print('%d，%d，%d' % (0, 1, 0))

name1 = 'Python'
print('I am learning %s' % name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。

# format()格式化函数：str.format()
print('\n{}{}'.format('数字：', 0))  # 优势1：不用担心用错类型码。
print('{}，{}'.format(0, 1))  # 不设置指定位置时，默认按顺序对应。
print('{1}，{0}'.format(0, 1))  # 优势2：当设置指定位置时，按指定的对应。
print('{0}，{1}，{0}'.format(0, 1))  # 优势3：可多次调用format后的数据。

name2 = 'Python基础语法'
print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。

# 摘自菜鸟教程
# 摘自菜鸟教程 https://www.runoob.com/python/att-string-format.html
# CSDN 的好文章推荐 https://blog.csdn.net/jpch89/article/details/84099277
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))  # 解构写法

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


# 也可以向 str.format() 传入对象：
class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# 数字格式化
# 下表展示了 str.format() 格式化数字的多种方法：
print("{:.2f}".format(3.1415926))  # 输出 3.14

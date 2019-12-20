# 查看注释，运行代码。
import random
import time

# 用random函数在列表中随机抽奖，列表中只有3位候选者。

luckylist = ['海绵宝宝', '派大星', '章鱼哥']
# random模块中有个随机选取一个元素的方法：random.choice()。
a = random.choice(luckylist)  # 从3个人中随机选取1个人。
print('开奖倒计时', 3)
time.sleep(1)  # 调用time模块，控制打印内容出现的时间
print('开奖倒计时', 2)
time.sleep(1)
print('开奖倒计时', 1)
time.sleep(1)
# 使用三引号打印hellokitty的头像
image = '''
 /\_)o<
|      \\
| O . O|
 \_____/
'''
print(image)  # ……
print('恭喜' + a + '中奖！')  # 使用print函数打印幸运者名单

# 步骤2 封装
import random
import time


# 提示：将以下部分封装进函数
def lotto():
    luckylist = ['海绵宝宝', '派大星', '章鱼哥']
    a = random.choice(luckylist)
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜' + a + '中奖！')


lotto()

# 参考代码
# 查看注释，运行代码。
import random
import time


# 将抽奖程序封装成函数
def choujiang(q, w, e):  # 定义一个抽奖函数，带有3个参数，也就是3位候选人
    luckylist = [q, w, e]  # 定义一个中奖名单的列表
    a = random.choice(luckylist)  # 在中奖名单里面随机选择
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    image = '''
    /\_)o<
    |      \\
    | O . O|
    \_____/
    '''
    print(image)
    print('恭喜' + a + '中奖！')


choujiang('虚竹', '萧峰', '段誉')  # 调用函数

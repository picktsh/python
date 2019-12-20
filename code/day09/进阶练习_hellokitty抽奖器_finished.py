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
    print('恭喜 ' + a + ' 中奖！')


choujiang('虚竹', '萧峰', '段誉')  # 调用函数

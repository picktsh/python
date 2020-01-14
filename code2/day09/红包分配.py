import random


def red_packet(money, num):
    money = money * 100
    # 得到一个4个项 的数组
    ret = random.sample(range(1, money), num - 1)
    # 加一个最小值
    ret.append(0)
    # 加一个最大值
    ret.append(money)
    # 排序,从小到大
    ret.sort()
    print(ret)  # 随机 [0, 15, 29, 66, 86, 100]
    # 这一步最关键
    # lists = [(ret[i + 1] - ret[i]) / 100 for i in range(len(ret) - 1)]
    # 下面是步骤分解
    lists = []
    for i in range(len(ret) - 1):
        a = ret[i + 1] - ret[i]
        a = a / 100
        print(i, ret[i + 1], '-', ret[i], '=', a)
        lists.append(a)
        """
        随机
        0 15 - 0 = 0.15
        1 29 - 15 = 0.14
        2 66 - 29 = 0.37
        3 86 - 66 = 0.2
        4 100 - 86 = 0.14
        """
    return lists


print(red_packet(1, 5))  # 随机 [0.15, 0.14, 0.37, 0.2, 0.14]

"""
红包金额范围内随机取红包数量-1
得到一个数组
往数组中加入0和金额(最小值和最大值)
排序,从小到大
循环,依次递减 list[i+1]-list[i]
得到的差值放入一个新的数组
最终得到一个随机的数字数组(红包分配)
"""
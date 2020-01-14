import random


def red_packet(money, num):
    money = money * 100
    ret = random.sample(range(1, money), num - 1)
    ret.append(0)
    ret.append(money)
    ret.sort()
    lists = [(ret[i + 1] - ret[i]) / 100 for i in range(len(ret) - 1)]
    return lists


print(red_packet(100, 5))

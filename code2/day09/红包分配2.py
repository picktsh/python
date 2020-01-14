import random


def red(money, num):
    money = int(money * 100)
    li = random.sample(range(1, money), num - 1)
    li = li + [0, money]
    li.sort()
    return [(li[i + 1] - li[i]) / 100 for i in range(len(li) - 1)]


m = float(input('老板想发多少元的红包?'))
n = int(input('发多少个呢?'))
print('给您分配的方案:', red(m, n))

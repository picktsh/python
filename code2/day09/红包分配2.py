import random


def red(m, n):
    m = m * 100
    li = random.sample(range(1, m), n - 1)
    li = li + [0, m]
    li.sort()
    nli = [(li[i + 1] - li[i]) / 100 for i in range(len(li) - 1)]
    return nli


print(red(5, 2))

# 使用他人的模块

import time

print('第一句话，过两秒出现第二句。')
time.sleep(2)
print('第二句话。')

import random

a = random.randint(0, 100)  # 随机从0-100之间抽取一个数字
print(a)

print(random.__file__)  # 查看文件路径


# 我们熟悉的函数random.choice(list)，功能是从列表中随机抽取一个元素并返回。它的代码被找到了：
def choice(self, seq):
    """Choose a random element from a non-empty sequence."""
    try:
        i = self._randbelow(len(seq))
    except ValueError:
        raise IndexError('Cannot choose from an empty sequence')
    return seq[i]


# 另一个熟悉的函数random.randint(a,b)，功能是在a到b的范围随机抽取一个整数。它的代码也被找到了：

def randint(self, a, b):
    """Return random integer in range [a, b], including both end points."""
    return self.randrange(a, b + 1)

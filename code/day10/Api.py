import math
import random

print(math.ceil(1.2))  # 向上取整: 2
print(math.floor(1.2))  # 向下取整: 1
print(int(1.2))  # 向下取整: 1
print(round(1.2))  # 四舍五入: 1
# 分别取
print(math.modf(4.25))  # (0.25, 4.0)
print(math.modf(4.33))  # (0.33000000000000007, 4.0)
# 最后一个应该是0.33，但是浮点数在计算机中是无法精确的表示小数的，python采用IEEE 754规范来存储浮点数。
print(random.randint(10, 11))  # 范围内随机整数 a:开始范围,b:结束范围 开始值可结束值都包括在随机范围内

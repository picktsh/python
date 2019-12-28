import math


# 方法1，关键词：条件判断
def abs_value1():
    a = float(input('1.请输入一个数字：'))
    if a >= 0:
        a = a
    else:
        a = -a
    print('绝对值为：%f' % a)


# 方法2，关键词：内置函数
def abs_value2():
    a = float(input('2.请输入一个数字：'))
    a = abs(a)
    print('绝对值为：%f' % a)


# 方法3，关键词：内置模块
def abs_value3():
    a = float(input('3.请输入一个数字：'))
    a = math.fabs(a)
    print('绝对值为：%f' % a)


abs_value1()
abs_value2()
abs_value3()

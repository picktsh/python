# 工作量计算器
# 版本1.0-能用就好
# 注：size代表项目大小，number代表人数，time代表工时数量

# 工时计算
size = 1.5
number = 2
time = (size * 80 / number)
print('项目大小为1.5个标准项目，使用2个人力完成，则需要工时数量为：', time)

# 人力计算
size = 0.5
time = 20.0
number = (size * 80 / time)
print('项目大小为0.5个标准项目，如果需要在20.0个工时完成，则需要人力数量为：', int(number))


# 阶段2-稍作封装
# 工时计算
def estimated_time(size, number):
    time = size * 80 / number
    print(time)
    return time


# 人力计算
def estimated_number(size, time):
    number = size * 80 / time
    print(number)
    return number


# 调用工时计算函数
estimated_time(1.5, 2)
# 调用人力计算函数
estimated_number(0.5, 20)


# 参考答案
# 无需修改代码，直接运行即可

# 工时计算
def estimated_time(size, number):
    time = size * 80 / number
    print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))


# 人力计算
def estimated_number(size, time):
    number = size * 80 / time
    print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))


# 调用工时计算函数
estimated_time(1.5, 2)
# 调用人力计算函数
estimated_number(0.5, 20)

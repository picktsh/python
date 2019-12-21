# 工作量计算器
# 函数封装
# 先将下面的代码改造成两个子函数和一个主函数，并调用主函数。

import math


def estimated(types, size=1.0, number=None, time=None):
    if types == 1:
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))
    elif types == 2:
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))


def choice():
    types = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
    if types == 1:
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = None
        time = float(input('请输入工时数量：（可以输入小数）'))
        estimated(types, size, number, time)
    elif types == 2:
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        estimated(types, size, number, time)


def main():
    choice()


main()

# ####################################分割线###########################################

# 请直接运行体验的代码
import math


# 采集信息的函数
def myinput():
    choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size, number, time
        # 这里返回的是一个元组
    elif choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size, number, time
        # 这里返回的数据是一个元组


# 完成计算的函数
def estimated(my_input):
    # 把元组中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))
        # 工时计算
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))
    
    # 主函数


def main():
    my_input = myinput()
    estimated(my_input)


# 调用主函数
main()

print('程序结束')

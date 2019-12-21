# 版本3.0:精细打磨

import math


def estimated():
    types = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
    # 人力计算
    if types == 1:
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        time = float(input('请输入工时数量：（请输入小数）'))
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))
    # 工时计算
    elif types == 2:
        size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        number = float(input('请输入人力数量：（请输入整数）'))
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))


'请选择计算类型：（1-人力计算，2-工时计算）'
'请输入项目大小：（1代表标准大小，可以输入小数）'
'请输入人力数量：（请输入整数）'
'请输入工时数量：（请输入小数）'
estimated()
print('程序结束')

# ####################################分割线###########################################

# 直接运行体验代码即可

import math


def estimated(size=1, number=None, time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' % (size, time, number))
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' % (size, number, time))


choice = input('请选择计算类型：（1-人力计算，2-工时计算）')
if choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = None
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size, number, time)
elif choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    time = None
    estimated(size, number, time)

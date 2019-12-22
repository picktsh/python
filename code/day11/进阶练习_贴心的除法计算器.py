# #2回顾和升级
# 请你先运行代码一次，然后取消第9，10两行的注释后，再运行一次代码。
'''
num = [1, 2, 0, 3, 1.5, '6']
for x in num:
    try:  # 尝试执行下列代码
        print(6 / x)
    except ZeroDivisionError:
        print('0是不能做除数的！')
    # except TypeError:  # 当报错信息为TypeError，执行下面的语句。
    #     print('被除数必须是整值或浮点数！')

# 当你运行两次代码后，你就知道：try下面可以包含多个except，针对不同的报错，类似多个 elif。
'''
num = [1, 2, 0, 3, 1.5, '6']
for x in num:
    try:  # 尝试执行下列代码
        print(6 / x)
    except ZeroDivisionError:
        print('0是不能做除数的！')
    except TypeError:  # 当报错信息为TypeError，执行下面的语句。
        print('被除数必须是整值或浮点数！')

# 当你运行两次代码后，你就知道：try下面可以包含多个except，针对不同的报错，类似多个 elif。

# #2 动手实操
# 请你改造下面的代码，目标：不论输入了什么，程序都不会因报错而停止（即找到所有的报错类型）。

while True:
    print('\n欢迎使用除法计算器！\n')
    x = input('请你输入被除数：')
    y = input('请你输入除数：')
    try:
        z = float(x) / float(y)
        print(x, '/', y, '=', z)
    except ZeroDivisionError:
        print('0是不能做除数的！')
    except TypeError:  # 当报错信息为TypeError，执行下面的语句。
        print('被除数必须是整值或浮点数！')
    except ValueError:  # ValueError:，执行下面的语句。
        print('除数和被除数必须是整值或浮点数！')
    # 下面是 print函数的一种用法，用逗号隔开，可在同一行打印不同类型的数据。
    break  # 当成功运行一次除法运算后，退出程序。
print('程序结束')

# 参考代码
print('\n欢迎使用除法计算器！\n')

while True:
    try:
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x) / float(y)
        print(x, '/', y, '=', z)
        break  # 默认每次只计算一次，所以在这里写了 break。
    except ZeroDivisionError:  # 当除数为0时，跳出提示，重新输入。
        print('0是不能做除数的！')
    except ValueError:  # 当除数或被除数中有一个无法转换成浮点数时，跳出提示，重新输入。
        print('除数和被除数都应该是整值或浮点数！')
    
    # 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
    except(ZeroDivisionError, ValueError):
        print('你的输入有误，请重新输入！')
    
    # 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。
    except Exception:
        print('你的输入有误，请重新输入！')

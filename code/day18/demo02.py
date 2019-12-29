# 这里有一个条件判断，即根据输入的数是正数还是负数会有不同的操作，那么把流程图画出来就是：
# 请按流程图中的步骤写代码，完成求绝对值的功能

while True:
    try:
        R = float(input('请输入一个数字(正数,负数,浮点数都行)'))
        break
    except:
        print('别捣乱,请输入数字(正数,负数,浮点数都行)')
S = None
if R >= 0:
    S = R
else:
    S = -R

print(S)
print('程序结束')

"""
参考代码
"""
print('欢迎使用绝对值计算程序。')
R = float(input('请输入数字:'))
if R >= 0:
    S = R
elif R < 0:  # 这里可以用“else:”代替“elif R<0:”
    S = -R
print('所求绝对值是：' + str(S))

# 囚徒困境
# 请你补充代码，让两位囚徒输入自己的选择，将其存成变量a,b
while True:
    a = int(input('A,认罪吗?(1:认罪/0:不认罪)'))
    b = int(input('B,认罪吗?(1:认罪/0:不认罪)'))
    if not (a & b):
        print('都不认罪,各判3年')
        break
    # 避免死循环

# 请补充下面的代码，添加4种判决和跳出语句，让代码满足练习要求。
while True:
    # 为了简化操作,用1和0来代替,输入非数字时转换会报错
    a = int(input('A，你认罪吗？请回答(1:认罪/0:不认)'))
    b = int(input('B，你认罪吗？请回答(1:认罪/0:不认)'))
    if (not a) & (not b):
        print('都不认罪,各判3年')
        break
    elif a & b:
        print('都认罪,各判10年')
        break
    elif a & (not b):
        print('A认罪,A判1年,B判20年')
        break
    elif b & (not a):
        print('B认罪,B判1年,A判20年')
        break
    else:
        print('别捣乱，只能回答“1”或“0”！')
print('程序结束')

# 参考答案
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
        break
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
        break
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
        break
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了')
        break
    else:
        print('别捣乱，只能回答“认罪”或“不认”！')

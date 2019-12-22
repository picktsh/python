# 被动掉坑debug
# 明想用python写个程序，看看自己的存款每个月涨了多少倍。
# 可是发现程序报错，你能帮他找出错误，使程序重新运行吗？

'''
deposit = [100,300,900,2000,5000,0,2000]

for i in range(1, len(deposit)):
    times = deposit[i]/deposit[i-1]
    print('你的存款涨了%f倍'%times)
    
'''

# 练习
deposit = [100, 300, 900, 2000, 5000, 0, 2000]

for i in range(1, len(deposit)):
    try:
        times = deposit[i] / deposit[i - 1]
        print('你的存款涨了%f倍' % times)
    except ZeroDivisionError:
        print('存款没涨')

# 参考代码
deposit = [100, 300, 900, 2000, 5000, 0, 2000]

for i in range(1, len(deposit)):
    try:
        times = deposit[i] / deposit[i - 1]
        print('你的存款涨了%f倍' % times)
    except ZeroDivisionError:
        print('存款没涨')

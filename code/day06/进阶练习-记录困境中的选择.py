# 需要的变量放到开头，明显一些。

lists = []
count = 0
while True:
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    # 需要将每一对实验者的选择存起来。
    lists.append({'a': a, 'b': b})
    count += 1
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    elif a == '不认' and b == '不认':
        print('都判3年，太棒了')
        break
    else:
        print('别捣乱，只能回答“认罪”或“不认”！')

print('有 ' + str(len(lists)) + ' 对实验者参加了选择')
# 打印是第几对实验者做出了最优选择。
print('第 ' + str(count) + ' 对实验者做出了最优选择')

# 通过循环打印每一对实验者的选择。
for i in lists:
    print(i)

# 参考代码
# 参考代码
n = 0
list_answer = []

while True:
    n += 1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a, b])  # 用列表嵌套的方式来存放实验者的选择，也可用元组或字典。
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

print('第' + str(n) + '对实验者选了最优解。')

for i in range(n):
    # 注意数据类型的转换，以及计数起点的不同（0和1）
    print('第' + str(i + 1) + '对实验者的选择是：' + str(list_answer[i]))

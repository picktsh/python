"""
5练习3：在读写之间处理数据-1

在课堂上，我们已经见识过了：文件的一读一写之间，可以对数据进行一定的处理。
请你运行一次右侧的代码，重新体验一下那个过程。
"""
file1 = open('scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

final_scores = []

for i in file_lines:
    data = i.split()
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换
    result = data[0] + str(sum) + '\n'  # 结果就是学生姓名和总分
    print(result)
    final_scores.append(result)

print(final_scores)

sum1 = open('winner.txt', 'w', encoding='utf-8')
sum1.writelines(final_scores)
sum1.close()
"""
输出:
罗恩102
哈利383
赫敏561
马尔福275
['罗恩102\n', '哈利383\n', '赫敏561\n', '马尔福275\n']
"""

"""
6练习3：在读写之间处理数据-2

现在，我们计划对课堂上得到的“winner”文档再行处理一下。
让学员的成绩从高到低排列，然后放到新文档“winner_new.txt”。
"""
# 下面已经为你准备好了打开的代码和一些变量名的准备。
# 请你完成数据处理以及新建文档（同一个目录）的代码。
# 一个提示：可以用 print 作为检验代码，步步为营。

file1 = open('winner.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()
# ['罗恩102\n', '哈利383\n', '赫敏561\n', '马尔福275\n']
# ['罗恩102\n', '哈利383\n', '赫敏561\n', '马尔福275\n']

# dict_scores = {}
# list_scores = []
# final_scores = []
#
# for i in file_lines:
#     dict_scores[i] = i
#     list_scores.append(i)
#     final_scores.append(i)
#     pass
#
# print(dict_scores)
# print(list_scores)
# print(final_scores)


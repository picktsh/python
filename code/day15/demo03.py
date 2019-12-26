# 小练习
"""
现在有这样一个叫scores.txt的文件，里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。

这里是文件内容，你可以在自己的电脑里新建一个scores.txt来操作。

罗恩 23 35 44
哈利 60 77 68 88 90
赫敏 97 99 89 91 95 90
马尔福 100 85 90



"""

file1 = open('./scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()
print(file_lines)

# ['罗恩 23 35 44\n', '哈利 60 77 68 88 90\n', '赫敏 97 99 89 91 95 90\n', '马尔福 100 85 90']
"""
你看到了，readlines() 会从txt文件取得一个列表，列表中的每个字符串就是scores.txt中的每一行。而且每个字符串后面还有换行的\n符号。

这样一来，我们就可以使用for循环来遍历这个列表，然后处理列表中的数据，请看第五行代码：
"""

file1 = open('./scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

for i in file_lines:  # 用for...in...把每一行的数据遍历
    print(i)  # 打印变量i

"""
罗恩 23 35 44
哈利 60 77 68 88 90
赫敏 97 99 89 91 95 90
"""

"""
这4个列表的第0个数据是姓名，之后的就是成绩。我们需要先统计各人的总成绩，然后把姓名和成绩放在一起。
还是可以用for...in...循环进行加法的操作，请看第8行的代码：
"""
file1 = open('scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

for i in file_lines:
    data = i.split()
    sum = 0  # 先把总成绩设为0
    for score in data[1:]:  # 遍历列表中第1个数据和之后的数据
        sum = sum + int(score)  # 然后依次加起来，但分数是字符串，所以要转换
    result = data[0] + str(sum)  # 结果就是学生姓名和总分
    print(result)

"""
接下来就是把成绩写入一个空的列表，因为这样才有助于我们之后写入一个txt文件。
"""
file1 = open('scores.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

final_scores = []  # 新建一个空列表

for i in file_lines:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum = sum + int(score)
    result = data[0] + str(sum) + '\n'  # 后面加上换行符，写入的时候更清晰。
    final_scores.append(result)  # 每统计一个学生的总分，就把姓名和总分写入空列表

"""
好啦，那我们就已经处理好了，就差写入文件啦。大家可以从第15行开始看：
"""
file = open('scores.txt', 'r', encoding='utf-8')
file_lines = file.readlines()
file.close()

final_scores = []

for i in file_lines:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum = sum + int(score)
    result = data[0] + str(sum) + '\n'
    final_scores.append(result)

winner = open('winner.txt', 'w', encoding='utf-8')
winner.writelines(final_scores)
winner.close()
# 16行的代码是以writelines()的方式写进去，为什么不能用write()？因为final_scores是一个列表，而write()的参数必须是一个字符串，而writelines()可以是序列，所以我们使用writelines()。

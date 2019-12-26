"""
练习3-参考代码

如果你成功写出了代码，先运行参考代码，你会发现并没有什么变化。
因为“winner_new.txt”已经存在，且处理方式不变（相当再写入了一次排序后的成绩）。
然后，请你将代码28行的“sort(reverse=True)”括号中的“reverse=True”去掉。
再运行一下，看下“winner_new”文档里的数据发生了什么变化。
如果你刚刚没有成功写出代码，可以通过参考代码，找到自己哪里出了bug，然后纠正。
"""

# 下面注释掉的代码，皆为检验代码（验证每一步的思路和代码是否达到目标，可解除注释后运行）。

file1 = open('winner.txt', 'r', encoding='utf-8')
file_lines = file1.readlines()
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

# print(file_lines)
# print(len('\n'))

# 打印结果为：['罗恩102\n', '哈利383\n', '赫敏570\n', '马尔福275\n']
# 经过测试，发现'\n'的长度是1。所以，名字是“第0位-倒数第5位”，分数是“倒数第4位-倒数第二位”。
# 再根据“左取右不取”，可知：name-[:-4],score-[-4:-1]

for i in file_lines:  # i是字符串。
    print(i)
    name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
    score = int(i[-4:-1])  # 取出成绩
    print(name)
    print(score)
    dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
    list_scores.append(score)

# print(list_scores)
list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
# print(list_scores)

for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    # print(result)
    final_scores.append(result)

print(final_scores)  # 最终结果

winner_new = open('winner_new.txt', 'w', encoding='utf-8')
winner_new.writelines(final_scores)
winner_new.close()

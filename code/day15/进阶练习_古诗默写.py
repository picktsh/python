"""
1练习介绍

练习目标
这个练习，会让你学会一种方法，可以直接修改原文件中的数据。

练习要求
语文老师将一些古诗存在txt文档里，一句一行。
最近，他计划抽一些古诗，自己设置一些空来让学生默写。
请你用代码帮老师完成这项工作（只要处理了一个文档，加上循环就能处理无数个文档了）。
"""
"""
2 明确目标
请看右侧的讲解，明确我们要达成的目标。
"""
# 由于系统原因，这里修改后的test.txt不会即时显示变化，你需要重新打开文件-root下的test.txt。
# 或者在本地新建文件夹，复制test.txt，在本地运行这段代码。

with open('test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 这时，lines 的数据存放在内存里。
print(lines)  # 将读取到的内容打印出来，发现实际上读到的是带换行符的字符串。
with open('test.txt', 'w', encoding='utf-8') as new:
    for line in lines:  # 在内存中，对数据进行处理，然后再写到文档里，覆盖之前的内容。
        if line not in ['0\n', '1\n']:  # 注意：这里的条件要根据上面打印出的数据写。
            new.write(line)

# 请你根据学到的新知识，在下面完成对文档“poem1.txt”的修改。
# 你可以处理命名为“poem1”的文档，参考代码会处理“poem1.txt”。
list_test = ['一弦一柱思华年。\n', '只是当时已惘然。\n']  # 将要默写的诗句放在列表里。
with open('poem2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
with open('poem2_new.txt', 'w', encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)

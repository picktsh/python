"""
1.练习介绍

练习目标
通过这个练习，我们会用模块去实现上一关卡的选做题“古诗默写”。

练习要求
这个练习，我们会接触一个新的Python内置模块：os（文件/目录方法）。
这个模块中的许多方法，配合文件读写以及数据处理，可以让一些工作得以自动化。
当然，在一个练习里，我们不会奢求那么多，先体验一下os模块里的3个方法即可。
"""
"""
代码回顾
我们先回顾一下不用模块是如何出古诗默写题的：
"""
list_test = ['一弦一柱思华年。\n', '只是当时已惘然。\n']

with open('poem1.txt', 'r') as f:
    lines = f.readlines()

with open('poem1.txt', 'w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

"""
os 模块中的替换方法

可能你会觉得这么操作更麻烦，但假设要你处理大量的文档，模块会让你的代码更清晰更简洁。
"""
# 同样，运行后重新打开文件查看变化
import os

with open('test.txt', 'r') as f:
    lines = f.readlines()

with open('test_new.txt', 'w') as new:  # 新建一个文档
    for line in lines:
        if line not in ['0\n', '1\n']:
            new.write(line)

# 可以先运行一次代码，然后，再将下面代码的注释取消，再运行一次。
os.replace('test_new.txt', 'test.txt')  # 语法：os.replace(file1,file2)，将file1重命名为file2，将其替代。

# 请你根据上面的方法，将之前的代码改为用模块 os 实现（可选文档poem2）。
# 在改代码之前，可以先将上面的代码注释，然后取消下面代码的注释。

list_test = ['一弦一柱思华年。\n', '只是当时已惘然。\n']

with open('poem2.txt', 'r') as f:
    lines = f.readlines()

with open('poem2.txt', 'w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

"""
参考代码
"""

import os

list_test = ['一弦一柱思华年。\n', '只是当时已惘然。\n']

with open('poem3.txt', 'r') as f:
    lines = f.readlines()

with open('poem_new.txt', 'w') as new:
    for line in lines:
        if line in list_test:
            new.write('____________。\n')
        else:
            new.write(line)

os.replace('poem_new.txt', 'poem3.txt')

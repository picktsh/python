"""
1. 练习介绍

练习目标
我们会通过今天的作业，用代码模拟一种现实中的场景：滚动的广告牌。

练习要求
实际生活中，有些广告牌是单行滚动的字体。
这个练习会通过新旧知识的结合，用Python实现对这种效果的模拟。
"""
"""
步骤讲解
在这个需求下，稍稍分析即可得：
广告显示：打印字符串；
广告滚动：字符串的改变和循环（注：字符串和列表一样，可以用偏移量来提取数据）。另外，循环的速度影响滚动速度，可以用 time.sleep() 来控制。
"""
"""
2 提出产品需求，形成技术方案

由于是练习，所以是没有让每个人根据自己的生活经验来提需求。
而是直接给定了产品需求：用Python代码模拟单行的滚动广告。
初步形成的技术方案是：print+字符串+循环+time模块（控制滚动速度）。
"""
"""
3. 完成程序代码

为了让这种模拟和实际的更接近，补充一个模块中的方法。
请你试着运行右侧的代码，然后将其注释掉，再用代码完成对广告牌的模拟，广告词可以自己起。
对了，正常的滚动广告是无限循环的。不过，你可以在代码中设置循环次数，只要保证效果即可。

"""
# 请运行下面的代码，看下效果，然后注释。

import os, time

for i in range(10):
    # os.system('clear')  # linux/os x系统 (clear)；windows 系统中，这个命令是 os.system('cls')，效果：清屏。
    print("\r这是第 {} 遍循环".format(i), end='')
    time.sleep(1)
print('程序结束')

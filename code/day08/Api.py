# 把 A 组成绩赋值给一个新列表，用来存合并的成绩——这个细节要注意！
list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
list3 = list1
list3.extend(list2)  # 继承语法
print(list3)

# list.sort() 排序
list = [91, 95, 97, 99, 92, 93, 96, 98]
list.sort()  # 改变原数组,返回值 None
print(list)

# sorted(list) 排序
list = [91, 95, 97, 99, 92, 93, 96, 98]
print(sorted(list))

#  2、字符串排序
StrList = ['fb', 'bx', 'csw', 'qb', 'qqa', 'eeeed']
StrList.sort()
print(StrList)  # 字符串列表是按照第一个字符的大小排序的
# 输出：['Fast', 'Smooth', 'fast', 'is', 'is', 'smooth']

# 2.2忽略大小写，按abcd顺序
StrList.sort(key=str.lower)
print(StrList)  # 输出：['Fast', 'fast', 'is', 'is', 'Smooth', 'smooth']

# 2.3按照字符串长度排序
StrList.sort(key=len)
print(StrList)  # 输出：['is', 'is', 'fast', 'Fast', 'Smooth', 'smooth']

StrList.sort(key=len, reverse=True)  # 反序
print(StrList)  # 输出：['Smooth', 'smooth', 'fast', 'Fast', 'is', 'is']

# sorted()适用于任何可迭代容器，list.sort()仅支持list（本身就是list的一个方法）

# 我们会帮老师计算出两组的平均分，并挑出那些在平均分之下的成绩。
scores = [91, 95, 97, 99, 92, 93, 96, 98]
sSum = sum(scores)  # 求和

# 新的库
# 新的库
# 新的库
import numpy as np  # 导入 numpy库，下面出现的 np 即 numpy库

average = np.mean(scores)  # 一行解决。
# 下面展示一种NumPy数组的操作，感兴趣的同学可以自行去学习哈。
scores3 = np.array(scores)
print(' 低于平均成绩的有：{}'.format(scores3[scores3 < average]))
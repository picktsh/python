# 我们会帮老师计算出两组的平均分，并挑出那些在平均分之下的成绩。
scores = [91, 95, 97, 99, 92, 93, 96, 98]
sSum = sum(scores)  # 求和
sAverage = sSum / len(scores)  # 平均分
print('总分: {}'.format(sSum))
print('平均分: {}'.format(sAverage))

# 筛选出低于平均分的同学
low = []
for i in scores:
    if i < sAverage:
        low.append(i)
print('低于平均分的同学有: {}'.format(low))

# 参考答案
# 参考答案
# 请你改造这个代码，用更简洁的方式满足老师的需求。

scores1 = [91, 95, 97, 99, 92, 93, 96, 98]
sum = 0
scores2 = []

for score in scores1:
    sum = sum + score
    average = sum / len(scores1)
    # 上面最好不要去数有几个学生，那样的话，学生数目发生变化就要调代码。
print('平均成绩是：{}'.format(average))

for score in scores1:
    if score < average:
        scores2.append(score)  # 少于平均分的成绩放到新建的空列表中
print(' 低于平均成绩的有：{}'.format(scores2))  # 上个关卡选做题的知识。

# 参考答案
# 参考答案 调用了 np 库的写法
import numpy as np  # 导入 numpy库，下面出现的 np 即 numpy库

scores1 = [91, 95, 97, 99, 92, 93, 96, 98]
scores2 = []

average = np.mean(scores1)  # 一行解决。
print('平均成绩是：{}'.format(average))

for score in scores1:
    if score < average:
        scores2.append(score)  # 少于平均分的成绩放到新建的空列表中
print(' 低于平均成绩的有：{}'.format(scores2))  # 上个关卡选做题的知识。

# 下面展示一种NumPy数组的操作，感兴趣的同学可以自行去学习哈。
scores3 = np.array(scores1)
print(' 低于平均成绩的有：{}'.format(scores3[scores3 < average]))

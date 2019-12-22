# 知识点debug
# 期末考试结束了，小加在教务系统查到了自己的几门必修课分数，他想通过python计算自己的平均分。
# 于是写了下面的代码，可是总是得不到结果，请帮纠正bug并跑通程序。
# 个人练习
scores = {'语文': 89, '数学': 95, '英语': 80}
sum_score = 0


def get_average(scores):
    global sum_score  # 总分期望使用的是全局的总分变量
    for subject, score in scores.items():
        sum_score += score
        print('现在的总分是:%d' % sum_score)
    ave_score = sum_score / len(scores)
    print('平均分是:%d' % ave_score)


get_average(scores)

# 参考答案
scores = {'语文': 89, '数学': 95, '英语': 80}


def get_average(scores):
    sum_score = 0  # sum_score 作为函数内部的局部变量，从而可以为函数所用。
    for subject, score in scores.items():
        sum_score += score
        print('现在的总分是%d' % sum_score)
    ave_score = sum_score / len(scores)
    print('平均分是%d' % ave_score)


get_average(scores)

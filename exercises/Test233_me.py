import math


def Pailie(list):
    # 内部合理储存变量,1.节省重复计算的CPU消耗;2.更好的进行断点测试
    colums = 5  # 每行显示的列(个)数
    lines = math.ceil(len(list) / colums)  # 总行数, 还可以尝试 range(10,20) 的第二个参数
    print('有: {} 个数据,每行显示 {} 个 总共: {} 行'.format(len(list), colums, lines))
    res = []  # 需要返回给调用者的返回结果
    # 这部分只进行逻辑处理
    for i in range(lines):
        start = i * colums  # 截取的开始位置
        end = start + colums  # 截取的结束位置
        row = list[start:end]
        # print(row)
        res.append(row)
    
    # 数据已经处理完,此处进行输出展示
    for i in range(len(res)):  # 此处有用到下标,稍微复杂一点点:先取长度再取范围,最后根据下标来取值
        item = res[i]
        # 当前序列号
        for j in range(len(item)):
            # j.join(',')
            num = i * colums + j + 1
            print('{}.{}'.format(num, item[j]), end='\t\t')
        print("")
    # 数据处理函数,一般只进行计算操作,并把计算结果返回出去
    return res


A5 = ['well', 'believe', 'fact', 'reason', 'heart', 'easy', 'worker', 'sport', 'artist', 'rock', 'perform', 'task',
      'basic', 'Christian', 'tool', 'cool', 'salt', 'bridge', 'guide', 'celebrate', 'physician', 'immediate',
      'practical', 'concert', 'burst', 'twist', 'dilemma', 'merchant', 'fever', 'zero', 'contrary', 'institute',
      'Arctic', 'sorrow', 'amusement', 'walnut', 'punctuate', 'vice', 'Antarctic', 'moustache', 'offence']
ListA = ['GMAT', 'NGEE', 'NCEE', 'CET4', 'CET6', 'TEM', 'TOEFL', 'GRE', 'IELTS', 'NONE']
ListB = ['GMAT', 'NGEE', 'NCEE']
ListC = ['GMAT', '考研', '高考', '四级', '六级', '英专', '托福', 'GRE', '雅思', '任意']
# Pailie(A5)
print(Pailie(A5))  # 期望返回结果 [[5],[5],...]

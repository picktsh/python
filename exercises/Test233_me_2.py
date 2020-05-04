import math

"""
    需求: 将一个列表的类容按照每5个换行排列输出
    @params lists 要展示的内容[]
    @params column 每行显示的列(个)数 默认值:5
    @params width # 每个单词的宽度; 默认值:20 PS:一般单词都不超过20个字母吧
    # TODO 暂不兼容中文字符,因为中文字符占2个宽度 [\u4e00-\u9fa5]
"""


def arrange(lists, column=5, width=20):
    # 内部合理储存变量;1.节省重复计算的CPU消耗;2.更好的进行断点测试
    lists_len = len(lists)  # 储存下传入的数组长度
    for i in range(lists_len):
        str = '{}.{}'.format(i + 1, lists[i])  # 要输出的内容:序号.内容
        end = ' ' * (width - len(str))  # 尾部填充的空格数量,!!!注意:中文字符宽度占2格需要特殊处理
        print(str, end=end)
        if (i + 1) % column == 0 or i + 1 == lists_len:  # 每到"列个数"的倍数时就换行; 最后一项换个行避免影响后续输出;
            print('')  # 恢复后续文本输出的默认色
    # -----核心功能已结束,以下为附加内容-----
    lines = math.ceil(lists_len / column)  # 最终页数
    # 颜色字语法: \033[显示方式; 前景色; 背景色m******\033[0m  想看更多请自行百度
    print('有\033[31m {} \033[0m个数据,每行显示\033[32m {} \033[0m个,总共\033[34m {} \033[0m行'.format(lists_len, column, lines))


data_1 = ['fact', 'believe', 'fact', 'reason', 'heart', 'easy', 'worker', 'sport', 'artist', 'rock', 'perform', 'task',
          'basic', 'Christian', 'tool', 'cool', 'salt', 'bridge', 'guide', 'celebrate', 'physician', 'immediate',
          'practical', 'concert', 'burst', 'twist', 'dilemma', 'merchant', 'fever', 'zero', 'contrary', 'institute',
          'Arctic', 'sorrow', 'amusement', 'walnut', 'punctuate', 'vice', 'Antarctic', 'moustache', 'offence']
data_2 = ['GMAT', 'NGEE', 'NCEE', 'CET4', 'CET6', 'TEM', 'TOEFL', 'GRE', 'IELTS', 'NONE']
data_3 = ['GMAT', '考研', '高考', '四级', '六级', '英专', '托福', 'GRE', '雅思', '任意']
# 测试数据
arrange(data_3, 3, 25)

print('-----程序结束-----')

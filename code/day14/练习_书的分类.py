"""
1.练习介绍

练习目标
利用类的继承，创建一个Book类的子类。

练习要求
在Book类的基础上，创建一个子类FictionBook类表示虚构类图书，并改造初始化方法，增加一个默认参数type = '虚构类'。
再利用str()方法打印出FictionBook类实例的相关信息。
"""
"""
2.书写代码

1.请你在右侧代码的基础上，创建一个子类FictionBook。
2.在子类改造父类的初始化方法，让程序能够打印出实例book的相关信息。
"""


class Book:
    
    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state


# 创建一个Book类的子类 FictionBook
class FictionBook(Book):
    def __init__(self, type, name, author, comment, state=0):
        Book.__init__(self, name, author, comment, state)
        self.type = type
    
    # 继承并定制父类的初始化方法，增加默认参数 type = '虚构类'，让程序能够顺利执行。
    
    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '类型：%s 名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.type, self.name, self.author, self.comment, status)


book = FictionBook('虚构类', '囚鸟', '冯内古特', '我们都是受困于时代的囚鸟')
print(book)

'''
让打印的结果为:
类型: 虚构类 名称：《囚鸟》 作者：冯内古特 推荐语：我们都是受困于时代的囚鸟
状态：未借出
'''

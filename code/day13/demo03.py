'''
## 类继承的练习
现在，请你尝试用代码完成下面的继承关系，按照下图类名和属性创建5个类，并打印出C4类的实例的属性name和num。
'''


class C0:
    name = 'C0'


class C1(C0):
    num = 1


class C2(C0):
    num = 2


class C3(C0):
    name = 'C3'


class C4(C1, C2, C3):
    pass


c = C4()
print(c.name)
print(c.num)

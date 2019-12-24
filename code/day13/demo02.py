'''
类的继承之多层继承
'''


# 你可以继续拓展上面的例子，或往上（地球人），或往下（深圳人）。跑个代码体验一下：
# 先阅读代码和注释，然后直接运行代码。
class Earthman:
    eye_number = 2


# 中国人继承了地球人
class Chinese(Earthman):
    eye_color = 'black'


# 广东人继承了中国人，同时也继承了地球人。
class Cantonese(Chinese):
    pass


yewen = Cantonese()
print(yewen.eye_number)  # 输出: 2
print(yewen.eye_color)  # 输出: black

'''
类的继承之多重继承
'''


# 一个类，可以同时继承多个类，语法为class A(B,C,D):。假设我们将“出生在江苏，定居在广东的人”设为一个类Yuesu，那么，它的创建语句则为class Yuesu(Yue,Su)。
# 所以，广东人创建的实例在调用属性和方法时，会先在左侧的父类中找，找不到才会去右侧的父类找。（可理解为“就近原则”）

class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'
    
    def diet(self):
        print('我们爱吃甜。')


class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'
    
    def diet(self):
        print('我们吃得清淡。')


class Yuesu(Yue, Su):
    pass


xiaoming = Yuesu()
# 先在 Yue类找，找到了，打印出来。
print(xiaoming.wearing)
# Yue类没有born_city，才去Su类找。
print(xiaoming.born_city)
# 方法调用，和属性调用一样，也符合就近原则。
xiaoming.diet()
'''
输出:
thin
Jiangsu
我们吃得清淡。

小结一下代码中体现的就近原则：越靠近子类（即越靠左）的父类，越亲近，越优先考虑。子类调用属性和方法时，会先在靠左的父类里找，找不到才往右找。
'''

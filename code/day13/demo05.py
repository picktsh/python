'''
类 定制 练习
'''


# 提示：初始化方法的定制，和一般的实例方法的定制是一样的。
class Chinese:
    def __init__(self, greeting='你好', place='中国'):
        self.greeting = greeting
        self.place = place
    
    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))


# 请为子类完成定制，代码量：两行。
class Cantonese(Chinese):
    def __init__(self):
        Chinese.__init__(self, greeting='雷猴', place='广东')


yewen = Cantonese()
yewen.greet()

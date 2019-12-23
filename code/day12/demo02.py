# 创建类的两个关键点
# 殊参数：self
class Chinese:
    
    def greeting(self):
        print('很高兴遇见你')
    
    def say(self):
        self.greeting()
        print('我来自中国')


person = Chinese()
# 创建实例person
person.say()


# 调用say()方法

# 综上，所以我们说self代表的是类的实例本身，方便数据的流转。对此，我们需要记住两点：
# 第一点：只要在类中用def创建方法时，就必须把第一个参数位置留给 self，并在调用方法时忽略它（不用给self传参）。
# 第二点：当在类的方法内部想调用类属性或其他方法时，就要采用self.属性名或self.方法名的格式。

# 特殊方法：初始化方法
# 阅读代码后直接运行
class Chinese:
    
    def __init__(self):
        print('很高兴遇见你，我是初始化方法')


person = Chinese()


# 是不是很神奇？我们只是创建了实例，还没有调用，初始化方法就自动执行了！
# 利用这个特性，在编写习惯上，我们会在初始化方法内部完成类属性的创建，为类属性设置初始值，这样类中的其他方法就能直接、随时调用。我们来看个例子：（阅读后直接运行）
class Chinese:
    def __init__(self):
        self.mouth = 1  # self.不能丢
        self.eye = 2
    
    def body(self):
        print('我有%s张嘴巴' % self.mouth)
        print('我有%s只眼睛' % self.eye)


person = Chinese()
person.body()


# 初始化方法传入参数

class Chinese:
    
    def __init__(self, name, birth, region):
        self.name = name  # self.name = '吴枫'
        self.birth = birth  # self.birth = '广东'
        self.region = region  # self.region = '深圳'
    
    def born(self):
        print(self.name + '出生在' + self.birth)
    
    def live(self):
        print(self.name + '居住在' + self.region)


person = Chinese('吴枫', '广东', '深圳')  # 传入初始化方法的参数
person.born()
person.live()

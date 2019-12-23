# 这一关重要的知识点，都整合在这一段代码里：

class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建
    
    def __init__(self, hometown):  # 类的初始化函数
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中...')  # 初始化中的语句
    
    def born(self):  # 实例方法的创建
        print('我生在%s;' % (self.hometown))


wufeng = Chinese('广东')  # 类的实例化
print(wufeng.eye)  # 打印实例属性
wufeng.born()  # 实例方法的调用

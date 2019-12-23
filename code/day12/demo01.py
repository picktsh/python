# 下面，请你现学现用，创建一个“中国人”的类，并为其创建一个属性和一个方法。
# 属性:眼睛是黑色的
# 方法:打印出'吃饭，选择用筷子。'
class Chinese:
    eye = 'black'
    
    def eat(self):
        print('吃饭，选择用筷子。')


wufeng = Chinese()  # 类的实例化
print(type(wufeng))
print(wufeng)
print(wufeng.eye)  # 实例调用类属性
wufeng.eat()  # 调用类中的方法（传参不用管self）
'''
输出:
<class '__main__.Chinese'>
<__main__.Chinese object at 0x0000018B53FA2D88>
black
吃饭，选择用筷子。
'''


class Computer:
    screen = True
    
    def start(self):
        print('电脑正在开机中……')


my_computer = Computer()
print(type(my_computer))
print(my_computer)
'''
# 输出:
<class '__main__.Computer'>
<__main__.Computer object at 0x7f7538540c50>
'''
print(my_computer.screen)
my_computer.start()
'''
输出:
True
电脑正在开机中……
'''


# 再啰嗦一句：类中创建的属性和方法可以被其所有的实例调用，而且，实例的数目在理论上是无限的。我们可以同时“新建”多个实例：


# 阅读代码后点击运行
class Chinese:
    eye = 'black'
    
    def eat(self):
        print('吃饭，选择用筷子。')


# 类的实例化：创建多个实例
wufeng = Chinese()
jiangjiang = Chinese()
kaxi = Chinese()

print(jiangjiang.eye)
wufeng.eat()
kaxi.eat()

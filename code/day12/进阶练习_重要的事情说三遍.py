# 先打招呼
# 要让机器人跟我们打招呼，至少要告诉 ta 两个信息：一是 ta 的名字，二是你的称呼。
# 请你根据课堂所学（初始化方法即可）及之前已经掌握的知识，让 ta 先和你打个招呼。

# 这个代码只要用到类中的初始化方法和类的实例化。
# 在完成代码后，请复制到你的本地（下一步要用）。

class Robot:
    def __init__(self, named='', name=''):
        self.named = named
        self.name = name
        self.wish = ''
    
    def hello(self):
        print('你好，{}。我是{}。遇见你，真好。'.format(self.named, self.name))
    
    def say_wish(self, wish):
        self.wish = wish
        print('{}的愿望是:'.format(self.named))
        for i in range(3):
            print(self.wish)


robot = Robot('崛起', '瓦力')
robot.hello()
robot.say_wish('成为Python大佬!')


# 参考代码
class Robot:
    def __init__(self):
        self.name = input('我现在刚诞生，还没有名字，帮我起一个吧。')
        self.master = input('对了，我要怎么称呼你呢？')
        print('你好%s，我叫%s。很开心，遇见你~' % (self.master, self.name))
    
    def say_wish(self):
        wish = input('告诉一个你的愿望吧：')
        print(self.master + '的愿望是：')
        # 这里也可以用字符串的格式化，不过，用循环语句的话，之后改复述次数会方便些。
        for i in range(3):
            print(wish)


robot1 = Robot()
robot1.say_wish()

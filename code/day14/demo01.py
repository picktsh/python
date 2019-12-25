"""
定义Book类
icon
根据需求，每本书的基本属性都要有四个：书名、作家、推荐语和借阅状态。所以，我们可以利用初始化方法__init__，让实例被创建时自动获得这些属性。

icon
请你小试牛刀，写出初始化方法的代码，确保后面两行的代码能够顺利执行，打印出作者名卡尔维诺。
"""


class Book:
    def __init__(self, name, author, title, status=0):
        self.name = name
        self.author = author
        self.title = title
        self.status = status


book = Book('看不见的城市', '卡尔维诺', '献给城市的最后一首爱情诗', '未借出')
print(book.author)

""""
参考答案
借阅状态state采用默认参数，用0来表示'未借出'，1来表示'已借出'。
"""


class Book:
    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
    # 分别表示书名、作者、推荐语和借阅状态


book = Book('看不见的城市', '卡尔维诺', '献给城市的最后一首爱情诗')
# state为默认参数，如无修改必要不用传递
print(book.author)

"""
那么，我们可以在初始化方法的基础上定义一个show_info()方法，打印出每本书的信息：

名称：《像自由一样美丽》 作者：林达 推荐语：你要用光明来定义黑暗，用黑暗来定义光明。
状态：未借出
"""


class Book:
    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
    
    def show_info(self):
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)


book1 = Book('像自由一样美丽', '林达', '你要用光明来定义黑暗，用黑暗来定义光明')
# 传入参数，创建实例
print(book1.show_info())
# 调用实例方法show_info()，打印出返回值

class Book:

    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        if self.state == 0:
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)
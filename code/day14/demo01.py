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
    
    def __init__(self, name, author, comment, state=0):
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


# 为了方便调试，验证代码是否写对了，我们可以先往书籍系统里添加几本书籍，也就是创建Book类的实例对象。
class Book:
    def __init__(self, name, author, comment, state=0):
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


class BookManager:
    books = []
    
    # 创建一个列表，列表里每个元素都是Book类的一个实例
    
    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        # 创建三个实例对象
        
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
        # 往列表依次添加元素，注意调用类属性books时，self不能丢
        # self.books = [book1, book2, book3]
        # 上面三行代码，可简化为一行，即直接创建列表。这种情况下，可不用在前面创建空列表。


manager = BookManager()

"""
验证成功。book1，book2，book3，都是Book类的实例对象。又因为对象本身有__str__方法，所以当打印对象时，就会打印出该方法中的返回值。
发现了吗？这个结果和我们想要定义的显示书籍信息的方法show_all_book()是一样的，所以我们可以把最后几行代码封装成方法。
"""


class BookManager:
    books = []
    
    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
    
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借出书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
    
    def show_all_book(self):
        for book in self.books:
            # self是实例对象的替身
            print(book)


manager = BookManager()
manager.menu()
# 完美！那么打印书籍信息的方法我们就讲到这。接下来我们来看第二个功能：添加书籍add_book()。

"""
估摸着是时候给你练手的机会了。请你在下面代码的基础上补充好add_book(self)的代码，尝试录入一本你喜欢的书，再跳回到查询功能，看是否运行成功。
点击代码框的放大功能方便编写哦～
"""


class Book:
    
    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
    
    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)


#
class BookManager:
    books = []
    
    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
    
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            else:
                break
    
    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')
    
    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者名称：')
        new_comment = input('请输入推荐语：')
        # 获取书籍相应信息，赋值给属性
        new_book = Book(new_name, new_author, new_comment)
        # 传入参数，创建Book类实例new_book
        self.books.append(new_book)
        print('书籍录入成功！\n')


manager = BookManager()
# manager.add_book()

"""
接下来，来看第三个功能：借阅书籍lend_book()。这是最关键的一环，也是最容易出错的一环。所以，要集中注意力哦。
这里有两个要点：1. 怎么判断这本书在不在系统里；2.怎么判断这本书有没有被借走。
其次，如果书在系统里，有没有被借走可以根据实例属性state来判断，0表示'未借出'，1表示'已借出'。
"""
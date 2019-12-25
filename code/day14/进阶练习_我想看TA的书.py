"""
1.练习介绍

练习目标
在原有代码的基础上做一些优化，让用户输入作者名，就能打印出系统里该作者所有书籍的相关信息。

练习要求
新建一个类的方法，让程序能够根据作者名来展示相关书籍的信息。
"""
"""
步骤讲解
练习目标：
在原有代码的基础上做一些优化，让用户输入作者名，就能打印出系统里该作者所有书籍的相关信息。

练习要求：
新建一个类的方法show_author_book()，让程序能够根据作者名来展示相关书籍的信息。
"""
"""
2.书写代码

请你阅读右侧代码，在此基础上，补充show_author_book()相关代码，实现根据作者名打印相关书籍信息的功能。
因为代码已经创建好了3个Book实例，代码运行后预期实现效果：
输入'三毛'，系统就会打印出两本书的相关信息。
输入'毛姆'，系统就会打印出一本书的相关信息。
输入'二毛', 系统就会打印出'很可惜，我们暂时没有收录这位作者的作品'
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


class BookManager:
    authors = []
    
    # 创建一个存放作者名的列表
    def __init__(self):
        book1 = Book('撒哈拉的故事', '三毛', '我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book2 = Book('梦里花落知多少', '三毛', '人人都曾拥有荷西，虽然他终会离去。')
        book3 = Book('月亮与六便士', '毛姆', '满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1, book2, book3]
        # 将三个实例放在列表books里
        self.authors.append(book1.author)
        self.authors.append(book2.author)
        self.authors.append(book3.author)
        # 将三个实例的作者名添加到列表author里
    
    def menu(self):
        while True:
            print('1.查询书籍')
            print('2.退出系统')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_author_book()
                # 调用方法
            else:
                print('感谢使用！')
                break
    
    def show_author_book(self):
        author = input('你想找谁的书呢？')
        # 请在此处补充该方法的代码
        for i in self.authors:
            if author == i:
                # 接下来找书
                for b in self.books:
                    if author == b.author:
                        print(b)
                # 找到这个作者之后,循环书籍列表之后退出循环
                break
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')


manager = BookManager()
manager.menu()

'''
一个思路：
1. 先用条件判断语句判断该作者在不在列表authors里，如果不在就打印'很可惜，我们暂时没有收录这位作者的作品'
2. 如果在，就遍历列表books的每个实例，当实例属性author与输入的作者名相等，就打印该实例
'''


# 参考代码

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


class BookManager:
    authors = []
    
    def __init__(self):
        book1 = Book('撒哈拉的故事', '三毛', '我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book2 = Book('梦里花落知多少', '三毛', '人人都曾拥有荷西，虽然他终会离去。')
        book3 = Book('月亮与六便士', '毛姆', '满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1, book2, book3]
        self.authors.append(book1.author)
        self.authors.append(book2.author)
        self.authors.append(book3.author)
    
    def menu(self):
        while True:
            print('1.查询书籍')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_author_book()
            else:
                print('感谢使用！')
                break
    
    def show_author_book(self):
        author = input('请输入想查询作家的名称：')
        if author in self.authors:
            print(author + '的作品有：')
            for book in self.books:
                if book.author == author:
                    print(book)
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')


manager = BookManager()
manager.menu()

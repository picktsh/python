"""例如random模块的关键知识（也就是比较有用的函数和类方法），可以做成这样的笔记："""
import random  # 调用random模块

a = random.random()  # 随机从0-1之间抽取一个小数
print(a)

a = random.randint(0, 100)  # 随机从0-100之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串/列表/字典等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3)  # 随机从字符串/列表/字典等对象中抽取多个不重复的元素
print(a)

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)
"""
另外，我们还可以使用dir()函数查看一个模块，看看它里面有什么变量、函数、类、类方法。
"""
# 请直接运行并体验代码

import random  # 调用random模块

print(dir(random))
"""
甚至不是模块，我们也可以用这种方式自学：dir(x)，可以查询到x相关的函数，x可以是模块，也可以是任意一种对象。
"""

# 请直接运行并体验代码

a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))  # 把字符串相关的函数展示出来
d = ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
     '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
     '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
     '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
     'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
     'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
     'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
     'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
     'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

a = []  # 设置一个列表
print('列表：')
print(dir(a))  # 把列表相关的函数展示出来
d = ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
     '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
     '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
     '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
     '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
     'reverse', 'sort']

a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来
d = ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
     '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
     '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
     '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
     'setdefault', 'update', 'values']

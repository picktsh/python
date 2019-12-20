# len() 直接运行代码即可
a = len('万物的终极答案是42')
print(a)
b = len(['海伯利安', '基地', '三体'])
print(b)


# 提示：x ** y 表示 x的y次幂
def math(x):
    y = x ** 2 + x
    return y


print(math(10))
print(math(20))
print(math(30))


# 现在，请你写出一个能计算字符串长度的函数，然后传递参数'三根皮带，四斤大豆'来调用函数，并将结果打印出来。
def my_len(words):
    return len(words)


# 函数的参数是字符串
print(my_len('三根皮带，四斤大豆'))


# 接下来，我会用一个场景将例子串起来，这个场景就在本关标题里 —— 深夜食堂营业记！深夜食堂，开张！
# 直接运行代码即可
def opening():
    print('总有一种味道能温暖你～')
    print('深夜食堂正式开业啦！')
    print('欢迎来自五湖四海的你前来品尝!')


opening()


# 接下来我会用appetizer和course来表示开胃菜和主食
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)


menu('话梅花生', '牛肉拉面')


# 参数位置
# 参数位置
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course + '\n')
    # 还记得转义字符\n吧，表示换行


menu('牛肉拉面', '话梅花生')
menu('话梅花生', '牛肉拉面')

# 如果采用下面这种形式传递，就不需要理会参数位置
menu(course='牛肉拉面', appetizer='话梅花生')


# 默认参数
# 默认参数
def menu(appetizer, course, dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)


menu('话梅花生', '牛肉拉面')


# 因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。

# 它的格式比较特殊，是一个星号*加上参数名，它的返回值也比较特殊，我们来看看下面的例子。print(*o
def menu(*barbeque):
    return barbeque


order = menu('烤鸡翅', '烤茄子', '烤玉米')
# 括号里的这几个值都会传递给参数barbeque

print(order)  # ('烤鸡翅', '烤茄子', '烤玉米')
print(type(order))  # <class 'tuple'>

# 你会发现函数返回的是这样的结果：('烤鸡翅', '烤茄子', '烤玉米')，我们用type()函数可以知道这种数据类型叫作元组(tuple)

# print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)
# 可以看到第一个参数objects带了*号，为不定长参数——这也是为什么print()函数可以传递任意数量的参数。其余四个为默认参数，我们可以通过修改默认值来改变参数，对比一下下列代码的输出结果。
print('金枪鱼', '三文鱼', '鲷鱼')
print('金枪鱼', '三文鱼', '鲷鱼', sep='+')
# sep控制多个值之间的分隔符，默认是空格
print('金枪鱼', '三文鱼', '鲷鱼', sep='+', end='=?')
# end控制打印结果的结尾，默认是换行)

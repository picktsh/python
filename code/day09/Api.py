# 声明函数
def math(x):
    y = 3 * x + 5
    return y


# 函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
#      2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
def math(x):
    # 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
    # 规范：括号是英文括号，后面的冒号不能丢
    y = 3 * x + 5
    # 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
    return y


# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略

# 参数位置
# 参数位置
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course + '\n')
    # 还记得转义字符\n吧，表示换行
    # return None  # 如果不写 return 程序也会在结尾加上 return None


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

# random.choice() 随机选择 和return 返回多个值
import random

# 引入random模块

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


print(coupon(3))
print(coupon(6))

# ## 返回值解构
# 另外一种方式：我们也可以同时定义多个变量，来接收元组中的多个元素（看最后四行代码，直接运行即可）：
import random

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


dish, egg = coupon(7)
# 元组的两个元素分别赋值给变量dish和egg
print(dish)
print(egg)

# ##作用域  global
rent = 3000

variable_cost = 0


def cost():
    global variable_cost  # 使用全局的变量
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本费用是' + str(variable_cost))


def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))


cost()
sum_cost()

# global语句一般写在函数体的第一行，它会告诉Python，“我希望variable_cost是个全局变量，所以请不要用这个名字创建一个局部变量”。所以sum_cost()函数内部现在可以直接使用声明后的全局变量variable_cost。

# 函数的嵌套
# 函数的嵌套

# 再看下代码的注释，加深对这一过程的了解吧。
class Chinese:
    eye = 'black'
    
    def eat(self):
        print('吃饭，选择用筷子。')


class Cantonese(Chinese):
    # 通过继承，Chinese类有的，Cantonese类也有
    pass


# 验证子类可以继承父类的属性和方法，进而传递给子类创建的实例
yewen = Cantonese()
# 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)
# 子类创建的实例，可调用父类的属性
yewen.eat()


# 子类创建的实例，可调用父类的方法

# 也来试一试，为下面的父类Cat创建一个子类Ragdoll(布偶猫)，并用这个子类的实例来调用父类的属性和方法。
class Cat:
    tail = True
    
    def say(self):
        print('喵喵喵喵喵~')


class Ragdoll(Cat):
    pass


ragdoll = Ragdoll()
ragdoll.say()

'''
不过，很多类在创建时也不带括号，如class Chinese:。这意味着它们没有父类吗？
并不。实际上，class Chinese:在运行时相当于class Chinese(object):。而object，是所有类的父类，我们将其称为根类（可理解为类的始祖）。
我们可以用一个函数来验证这一点：函数isinstance()，可以用来判断某个实例是否属于某个类。
具体用法是输入两个参数（第一个是实例，第二个是类或类组成的元组），输出是布尔值（True 或 False）。跑下代码你就完全懂了：
'''
# 阅读代码和注释，直接运行

print(isinstance(1, int))
# 判断1是否为整数类的实例
print(isinstance(1, str))

print(isinstance(1, (int, str)))
# 判断实例是否属于元组里几个类中的一个

'''
好。可以正式验证了：
'''


# 阅读完代码再运行。
class Chinese:
    pass


class Cantonese(Chinese):
    pass


gonger = Chinese()
# 宫二，电影《一代宗师》女主，生于东北
yewen = Cantonese()
# 叶问，电影《一代宗师》男主，生于广东

print('\n验证1：子类创建的实例同时也属于父类')
print(isinstance(gonger, Chinese))
print(isinstance(yewen, Chinese))

print('\n验证2：父类创建的实例不属于子类。')
print(isinstance(gonger, Cantonese))

print('\n验证3：类创建的实例都属于根类。')
print(isinstance(gonger, object))
print(isinstance(yewen, object))

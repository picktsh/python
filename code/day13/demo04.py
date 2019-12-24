'''
类的定制，要怎么写？
定制，可以新增代码
'''


class Chinese:
    eye = 'black'
    
    def eat(self):
        print('吃饭，选择用筷子。')


class Cantonese(Chinese):  # 类的继承
    native_place = 'guangdong'  # 类的定制
    
    def dialect(self):  # 类的定制
        print('我们会讲广东话。')


yewen = Cantonese()
print(yewen.eye)
# 父类的属性能用
print(yewen.native_place)
# 子类的定制属性也能用
yewen.eat()
# 父类的方法能用
yewen.dialect()
# 子类的定制方法也能用

# 我们可以在子类下新建属性或方法，让子类可以用上父类所没有的属性或方法。这种操作，属于定制中的一种：新增代码。
'''
定制，也可重写代码
'''


class Chinese:
    def land_area(self, area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % area)


class Cantonese(Chinese):
    # 直接对方法进行重写
    def land_area(self, area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % int(area * 0.0188))


gonger = Chinese()
yewen = Cantonese()
gonger.land_area(960)
yewen.land_area(960)

'''
不过，这个其实是不好的示范。虽然目的达成了，但直接重写并不优雅（有点类似洗去了旧方法，然后补上新方法）。
想一想：假设有34个子类需定制这个方法，都是直接重写。那么，假设父类的方法改变，如说法改为“我们脚下的大地的面积有960万平方公里”。那么，就需要将所有子类的代码中的说法也改变。
显然，这样对代码的维护很不友好。所以，下面介绍更优雅的重写方式：
'''


# 阅读代码后运行
class Chinese:
    
    def land_area(self, area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % area)


class Cantonese(Chinese):
    # 为参数 area 设置默认值。
    def land_area(self, area=960, rate=0.0188):
        Chinese.land_area(self, area * rate)  # 拿到父组件的方法,在参数上进行定制后输出
        

yewen = Cantonese()
yewen.land_area()
# 两个参数都有默认值，所以可以这么调用。

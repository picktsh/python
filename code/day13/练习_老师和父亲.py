"""
1:步骤讲解:
明确目标很重要（所以重复三遍）。
做到后面的步骤，可再点开左侧的“练习介绍”查看。

练习目标：
在这个作业，我们会通过对类属性这个切入点，温习类的继承和定制。

练习要求：
每个人都有好几个不同的身份，且不同身份都附带一些特定的特征（属性）和行为（方法）。
例如，有这样一群人：在学校时被归在老师，脸是严肃的；亲子关系中（parenthood）则被归到父亲，脸是甜蜜的。
下面，我们就以这群人为例，探索类属性在类的继承和定制中的传递和改变。
"""
"""
2.创建两个类：老师和父亲
首先，我们需要创建两个类，并为它们添加属性。
"""


# 直接运行代码即可。
class Teacher:
    face = 'serious'
    job = 'teacher'


class Father:
    face = 'sweet'
    parenthood = 'dad'


time1 = Teacher()  # 在time1这个时刻，那个男人角色是老师。
time2 = Father()  # 在time2这个时刻，那个男人角色是父亲。
print(time1.face)  # 时刻不同，角色不同，脸也不同。
print(time2.face)
""""
3.子类的继承和定制
请你创建两个子类，同时继承已有的两个类（注：多重继承）；
然后，在其中选个子类进行定制：将 face 属性的值改变为'gentle'；
再者，创建实例 time3、time4，以调用子类的 face 属性。
"""""


# 先补全代码，然后再运行。
# 可体会多重继承中的就近原则。
class Teacher:
    face = 'serious'
    job = 'teacher'


class Father:
    face = 'sweet'
    parenthood = 'dad'


class Husband(Teacher, Father):
    face = 'gentle'
    pass


class brother(Teacher, Father):
    pass


time3 = Husband()  # 在time3这个时刻，那个男人角色是老公。
time4 = brother()  # 在time4这个时刻，那个男人角色是兄弟。
print(time3.face)  # 时刻不同，角色不同，脸也不同。
print(time4.face)

"""
4.参考代码
"""


class Teacher:
    face = 'serious'
    job = 'teacher'


class Father:
    face = 'sweet'
    parenthood = 'dad'


class TeacherMore(Teacher, Father):
    pass


class FatherMore(Father, Teacher):
    face = 'gentle'


time3 = TeacherMore()
time4 = FatherMore()
print(time3.face)
print(time4.face)

"""
1.练习目标：
这个练习，主要是训练你对“子类的继承”的理解和运用。

练习要求：
练习会先提供一个类，用以记录学生学习 Python 的投入时间和有效时间。
需要你创建一个子类，为某一类学生提供定制化的记录方案。
步骤讲解
明确目标很重要（所以重复三遍）。
做到后面的步骤，可再点开左侧的“练习介绍”查看。

练习目标：
这个练习，主要是训练你对“子类的继承”的理解和运用。

练习要求：
练习会先提供一个类，用以记录学生学习 Python 的投入时间和有效时间。
需要你创建一个子类，为某一类学生提供定制化的记录方案。
"""
"""
2.用代码记录时间
请看代码：
"""

"""
# 请先读懂代码，再运行。
class Student:
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name, job=None, time=0.00, time_effective=0.00):
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective
    
    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate  # 有效时间=投入时间×学习效率


student1 = Student('韩梅梅')
print(student1.job)  # 输出: None
student1.count_time(10, 0.8)  # 学习效率为0.8 ,输出: 8.0
print(student1.time_effective)
"""

"""
通过类的定制升级代码

假设：编程开发人员学 Python 的话，学习效率很高，默认为1。
而且，job 的属性为 programmer。
请你补全右侧的代码，将其升级。
"""


class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.00):
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective
    
    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate


# 请你完成子类的定制（包括初始化方法和count_time函数）
class Programmer(Student):
    def __init__(self, name, job=None, time=0.00, time_effective=1):
        Student.__init__(self, name, job, time, time_effective)


# 通过两个实例，完成子类和父类的对比（可自行验证）
student1 = Student('韩梅梅')
student2 = Programmer(name='李雷', job='programmer')
student1.count_time(20, .8)
student2.count_time(20, 1)
print(student1.time_effective)
print(student2.time_effective)

"""
参考代码
"""


class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.00):
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective
    
    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate


class Programmer(Student):
    def __init__(self, name):
        Student.__init__(self, name, job='programmer', time=0.00, time_effective=0.00)
    
    def count_time(self, hour, rate=1):
        Student.count_time(self, hour, rate)


student1 = Student('韩梅梅')
student2 = Programmer('李雷')
print(student1.job)
print(student2.job)
student1.count_time(10, 0.8)
student2.count_time(10)
print(student1.time_effective)
print(student2.time_effective)

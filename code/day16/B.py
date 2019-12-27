a = '我是模块中的变量a'


def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')


class Go2:
    a = '我是类2中的变量a'
    
    def do2(self):
        print('函数“do2”已经运行！')


# 如果此文件是被其他文件导入则不会执行此代码,只有作为主程序的时候才会执行这段代码
if __name__ == '__main__':
    print('【载入模块时，所有语句都会被运行】')
    print(a)
    hi()
    b = Go2()
    print(Go2.a)
    b.do2()

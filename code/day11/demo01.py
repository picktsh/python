# bug 1：粗心

# 有一处错误
# a = input('请输入密码：')
# if a == '123456'
#     print('通过')
a = input('请输入密码：')
if a == '123456':
    print('通过')

# 有三处错误
'''
for x in range(10)：
     print（x）
'''
for x in range(10):
    print(x)

'''
while n<3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username = 'abc' and password = '123':
        print("登录成功")
        break
    else
        n=n+1
        print("输入有误")
else
    print("你输错了三次，登录失败")
'''

n = 0
while n < 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == 'abc' and password == '123':
        print("登录成功")
        break
    else:
        n = n + 1
        print("输入有误")
else:
    print("你输错了三次，登录失败")

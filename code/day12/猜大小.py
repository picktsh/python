secret = 24  # 设定秘密数字
while True:
    # 这里使用 while 和try...except 对用户输入非法字符可能导致程序报错进行处理
    while True:
        try:
            # 只有数字才能判断大小  先对 input的内容进行 类型转换成整数或浮点数 便于后面计算
            # guess = int(input('你来猜猜我的秘密数字是多少:'))  # 输入猜测数字
            guess = float(input('你来猜猜我的秘密数字是多少:'))  # 输入猜测数字
            break
        except Exception:
            print('只能输入整数或浮点数哦~,再试一次')
    
    # 数字对比
    if guess == secret:
        print('恭喜你,猜对了!')
        # 猜对了就退出循环,结束程序
        break
    elif guess > secret:
        print('猜大啦,再猜猜')
    elif guess < secret:
        print('猜小啦,再猜猜')

print('程序结束')

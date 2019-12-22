while True:
    txt = input('请输入点东西:')
    if txt:
        print('输入通过,退出while循环,继续做接下来的事情')
        break
    else:
        print('输入不通过,再试一次')
print('程序结束')

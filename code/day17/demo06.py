"""
因为循环次数不固定，所以我们选择while循环来做。我的这段代码是这样的，加了一个print()函数来确认结果：
"""
to_addrs = []
while True:
    a = input('请输入收件人邮箱：')
    # 输入收件人邮箱
    to_addrs.append(a)
    # 写入列表
    b = input('是否继续输入，n退出，任意键继续：')
    # 询问是否继续输入
    if b == 'n':
        break

print(to_addrs)

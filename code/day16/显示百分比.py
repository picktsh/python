import time

for i in range(11):
    time.sleep(0.5)
    print('\r当前进度：{0}{1}%'.format('▉' * i, (i * 10)), end='')
print('加载完成！')
# \r是将光标移到一行的开始，所以\r之后的内容会覆盖掉上次打印的内容，形成动态打印。
# \b是backSpace 退格按钮


"""
运行以下三行代码，你就能直观清晰地知道csv是什么。
"""
file = open('test.csv', 'a+')
# 创建test.csv文件，以追加的读写模式
file.write('美国队长,钢铁侠,蜘蛛侠')
# 写入test.csv文件
file.close()
# 关闭文件

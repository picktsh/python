# 思维不清debug

# 小强认识了一个新朋友叫旺财，他想让你给他取个外号，但他很不喜欢别人叫他小狗和汪汪，
# 于是写了一个程序让自己避免叫他这两个外号中的一个，可是不知为什么叫他小狗程序也没有警告。
not_bad_word = True
while not_bad_word:
    x = input('请给旺财取个外号：')
    if x == '小狗' and x == '汪汪':
        not_bad_word = False
        print('我生气了，不想理你了！')

print('对不起，以后我不会这么叫你了')

# 练习
not_bad_word = True
names = ['小狗', '汪汪']
while not_bad_word:
    x = input('请给旺财取个外号：')
    if x in names:  # 只要外号是两个中的一个，就会生气。
        not_bad_word = False
        print('我生气了，不想理你了！')

print('对不起，以后我不会这么叫你了')

# 参考代码
not_bad_word = True
while not_bad_word:
    x = input('请给旺财取个外号：')
    if x == '小狗' or x == '汪汪':  # 只要外号是两个中的一个，就会生气。
        not_bad_word = False
        print('我生气了，不想理你了！')

print('对不起，以后我不会这么叫你了')

# ?? 不命中判断时没有 退出程序
# ?? 什么时候你才会觉得名字可以了呢

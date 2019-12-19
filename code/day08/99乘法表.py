n = 9
for i in range(1, n + 1):
    str = ''
    for j in range(1, i + 1):
        str += '{0}×{1}={2}; '.format(j, i, i * j)
    print(str)
# for 最简化版本
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0}×{1}={2}'.format(j, i, i * j), end='  ')
    print('')
# for 条件退出版本
for i in range(1, 10):
    for j in range(1, 10):
        print('%d X %d = %d' % (j, i, i * j), end='  ')
        if i == j:
            print('')
            break
# while 条件退出版本
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j, i, i * j), end='  ')
        j += 1
    print('')
    i += 1

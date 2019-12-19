for i in range(1, 20 + 1):
    for j in range(1, i + 1):
        print('{0}×{1}={2}'.format(j, i, i * j), end='  ')
    print('')

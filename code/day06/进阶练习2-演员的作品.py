# 演员的作品
# 优质练习
movies = {
    '妖猫传': ['黄轩', '染谷将太'],
    '无问西东': ['章子怡', '王力宏', '祖峰'],
    '超时空同居': ['雷佳音', '佟丽娅'],
}

while True:
    actor = input('你想查询哪个演员？(0:退出):')
    # 输入 0 退出程序
    if actor == '0':
        break
    for mo in movies:
        if actor in movies[mo]:
            print(actor + ' 出演了电影: ' + mo)
            break
    else:
        print('没查到,再试一次')
print('程序结束')

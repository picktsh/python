import time
import random

# 后续代码 1秒后再执行
time.sleep(1)

# 调用random模块，与
a = random.randint(1, 100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
print(a)

# 【格式化字符串】
player_life = 120
player_attack = 100
print('血量：' + str(player_life) + ' 攻击：' + str(player_attack))
print('血量：%s 攻击：%s' % (player_life, player_attack))

i = 0
print(' \n——————现在是第' + str(i) + '局——————')  # 替换前
print('  \n——————现在是第 %s 局——————' % i)  # 替换后

print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))  # 替换前
print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))  # 替换后

print('敌人发起了攻击，【玩家】剩余血量' + str(player_life))  # 替换前
print('敌人发起了攻击，【玩家】剩余血量%s' % player_life)  # 替换后

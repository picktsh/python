print('【玩家】\n血量：100\n攻击：50')  # 自定义玩家角色的血量和攻击，用换行符'\n'来优化视觉
print('------------------------')  # 辅助功能，起到视觉分割的作用，让代码的运行结果更清晰

print('【敌人】\n血量：100\n攻击：30')
print('------------------------')

print('你发起了攻击，【敌人】剩余血量50')  # 人工计算敌人血量：100-50=50
print('敌人向你发起了攻击，【玩家】剩余血量70')  # 人工计算玩家血量：100-30=70
print('------------------------')

print('你发起了攻击，【敌人】剩余血量0')  # 双方同时攻击，若血量出现小于等于0，游戏结束
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')

print('敌人死翘翘了，你赢了！')  # 打印结果

# import time   #调用time模块
# time.sleep(secs)
# 使用time模块下面的sleep()函数，括号里填的是间隔的秒数（seconds，简称secs）
# time.sleep(1.5)就表示停留1.5秒再运行后续代码

import time  # 通常import语句会写到代码的开头

print('【玩家】\n血量：100\n攻击：50')
print('------------------------')
time.sleep(1.5)
# 暂停1.5秒，再继续运行后面的代码

print('【敌人】\n血量：100\n攻击：30')
print('------------------------')
time.sleep(1.5)
# 同上

print('你发起了攻击，【敌人】剩余血量50')
print('敌人向你发起了攻击，【玩家】剩余血量70')
print('------------------------')
time.sleep(1.5)

print('你发起了攻击，【敌人】剩余血量0')
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')
time.sleep(1.5)

print('敌人死翘翘了，你赢了！')

# 可以多运行几次，看看结果是不是随机生成的~

import random

# 调用random模块，与
a = random.randint(1, 100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
print(a)

# 提示：调用模块需在开头写上import 模块名，这里需要用到random模块
import random

HP = random.randint(100, 150)
ATK = random.randint(30, 50)
print('HP:' + str(HP))
print('ATK:' + str(ATK))

# 版本2
# 版本2
import time, random

player_life = random.randint(100, 150)
player_attack = random.randint(30, 50)
enemy_life = random.randint(100, 150)
enemy_attack = random.randint(30, 50)

print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
print('------------------------')
time.sleep(1)

while (player_life > 0) and (enemy_life > 0):
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    # player_life是整数型，所以拼接时要先用str()转换
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
    print('------------------------')
    time.sleep(1.5)
    # 为了体现出战斗回合，这里停顿1.5秒

# 版本3.0：打印战果，三局两胜
# 版本3.0：打印战果，三局两胜
# 练习
import time, random

# 生成双方角色，并生成随机属性。
player_life = random.randint(100, 150)
player_attack = random.randint(30, 50)
enemy_life = random.randint(100, 150)
enemy_attack = random.randint(30, 50)

# 展示双方角色的属性
print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
print('------------------------')
time.sleep(1)

# 双方PK
while player_life > 0 and enemy_life > 0:
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
    print('-----------------------')
    time.sleep(1.5)
    if player_life > 0 & enemy_life <= 0:
        print('我赢了')
    elif player_life <= 0 & enemy_life > 0:
        print('我输了')
    elif player_life == enemy_life:
        print('平局')

# 打印战果
# 提示1:有三种结果，需要用到多向判断 if...elif...else
# 提示2:判断条件为双方的血量情况

# 参考答案
import time, random

# 生成双方角色，并生成随机属性。
player_life = random.randint(100, 150)
player_attack = random.randint(30, 50)
enemy_life = random.randint(100, 150)
enemy_attack = random.randint(30, 50)

# 展示双方角色的属性
print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
print('------------------------')
time.sleep(1)

# 双方PK
while player_life > 0 and enemy_life > 0:
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
    print('-----------------------')
    time.sleep(1.5)

# 打印战果
if player_life > 0 and enemy_life <= 0:
    print('敌人死翘翘了，你赢了')
elif player_life <= 0 and enemy_life > 0:
    print('悲催，敌人把你干掉了！')
else:
    print('哎呀，你和敌人同归于尽了！')

# 三局两胜
# 三局两胜
# 练习
import time, random

# 生成双方角色，并生成随机属性。
player_life = random.randint(100, 150)
player_attack = random.randint(30, 50)
enemy_life = random.randint(100, 150)
enemy_attack = random.randint(30, 50)

# 展示双方角色的属性
print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
print('------------------------')
time.sleep(1)

# 双方PK
for i in range(1, 4):
    print('第' + str(i) + '句开始')
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
    print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
    print('-----------------------')
    time.sleep(1.5)

# 打印战果
if player_life > 0 and enemy_life <= 0:
    print('敌人死翘翘了，你赢了')
elif player_life <= 0 and enemy_life > 0:
    print('悲催，敌人把你干掉了！')
else:
    print('哎呀，你和敌人同归于尽了！')
# 参考
import time, random

for i in range(1, 4):
    time.sleep(1.5)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第' + str(i) + '局，ready go!——————')  # 作为局的标记

    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # 展示双方角色的属性
    print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    # 打印战果
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，你赢了')

    elif player_life <= 0 and enemy_life > 0:
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

# 最终版本
import time, random

player_victory = 0
enemy_victory = 0

for i in range(1, 4):
    time.sleep(2)  # 让局与局之间有较明显的有时间间隔
    print(' \n——————现在是第' + str(i) + '局——————')  # 作为局的标记

    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # 展示双方角色的属性
    print('【玩家】\n' + '血量：' + str(player_life) + '\n攻击：' + str(player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n' + '血量：' + str(enemy_life) + '\n攻击：' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # 双方PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量' + str(enemy_life))
        print('敌人向你发起了攻击，【玩家】剩余血量' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    # 打印最终战果
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

if player_victory > enemy_victory:
    time.sleep(1)
    print('【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('【最终结果：你输了！】')
else:
    print('【最终结果：平局！】')

# 最终版 使用 %* 简化版
import time
import random

player_victory = 0
enemy_victory = 0

for i in range(1, 4):
    time.sleep(1.5)
    print('  \n——————现在是第 %s 局——————' % i)
    # 对比之前：(' \n——————现在是第'+str(i)+'局——————')
    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
    print('-----------------------')
    time.sleep(1)

    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【敌人】剩余血量%s' % enemy_life)
        print('敌人向你发起了攻击，【玩家】的血量剩余%s' % player_life)
        print('-----------------------')
        time.sleep(1.2)

    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

if player_victory > enemy_victory:
    time.sleep(1)
    print('\n【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('\n【最终结果：你输了！】')
else:
    print('\n【最终结果：平局！】')

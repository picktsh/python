# 请你补充2行代码，完成方案1的思路验证。
goon = True
while goon:
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        goon = False

# 请你补充4行代码，完成方案1的思路验证。
again = True
while again:
    a2 = input('要继续游戏吗，请输入y继续，输入其他退出：')
    if a2 != 'y':
        again = False

import time
import random

again = True
while again:
    player_victory = 0
    enemy_victory = 0
    for i in range(1, 4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
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

    a2 = input('要继续游戏吗，请输入y继续，输入其他退出：')
    if a2 != 'y':
        again = False

import time
import random

again = True
while again:
    player_victory = 0
    enemy_victory = 0
    for i in range(1, 4):
        time.sleep(1)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100, 150)
        player_attack = random.randint(30, 50)
        enemy_life = random.randint(100, 150)
        enemy_attack = random.randint(30, 50)

        print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))
        print('------------------------')
        time.sleep(.5)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
        print('-----------------------')
        time.sleep(.5)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【玩家】剩余血量%s' % player_life)
            print('敌人向你发起了攻击，【敌人】的血量剩余%s' % enemy_life)
            print('-----------------------')
            time.sleep(.5)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory:
        time.sleep(.5)
        print('\n【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')
    else:
        print('\n【最终结果：平局！】')

    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')  # 在 while True 循环中设置跳出条件。
    if a1 == 'n':
        again = False
        break

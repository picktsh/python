import random

# 引入random模块

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


print(coupon(3))
print(coupon(6))

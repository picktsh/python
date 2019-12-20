# 返回多个值
import random

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


print(coupon(6))
print(type(coupon(6)))

# 另外一种方式：我们也可以同时定义多个变量，来接收元组中的多个元素（看最后四行代码，直接运行即可）：
import random

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


dish, egg = coupon(7)
# 元组的两个元素分别赋值给变量dish和egg
print(dish)
print(egg)

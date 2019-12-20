# 步骤讲解
# 发放奖金的要求如下：
# 工作时长不满六个月，发放固定奖金500元。
# 工作时长在六个月和一年之间(含一年)，发放奖金120元*月数（如8个月为960元）
# 工作时长在一年以上，发放奖金180元*月数 （如20个月为3600元）
# 我们可以定义两个函数，第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。

# 定义两个函数：第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。
# 最后传入参数('大聪'，14)调用第二个函数，打印结果'大聪来了14个月，获得奖金2520元'

def month(long):
    if long < 6:
        return 500
    elif 6 <= long <= 12:
        return 120 * long
    elif long > 12:
        return 180 * long


def bonus(name, months):
    month(months)
    print('{0} 来了 {1} 个月,获得奖金 {2} 元'.format(name, months, month(months)))


bonus('大聪', 14)


# 参考答案
def bonus(month):
    if month < 6:
        money = 500
        return money
    elif 6 <= month <= 12:
        money = 120 * month
        return money
    else:
        money = 180 * month
        return money


def info(name, month):
    gain = bonus(month)
    print('%s来了%s个月，获得奖金%s元' % (name, month, gain))


info('大聪', 14)

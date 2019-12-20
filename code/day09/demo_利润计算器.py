# 利润计算器
def div(num1, num2):
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + '%'
    return percent


def warning():
    print('Error: 你确定上个月一毛钱都不赚不亏吗？')


def main():
    while True:
        num1 = float(input('请输入本月所获利润'))
        num2 = float(input('请输入上月所获利润'))
        if num2 == 0:
            warning()
        else:
            print('本月的利润增长率：' + div(num1, num2))
            break


main()

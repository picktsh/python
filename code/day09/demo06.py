# 函数的嵌套
rent = 3000


def cost():
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))
    return variable_cost


def sum_cost():
    sum = rent + cost()
    print('本月的总成本是' + str(sum))


sum_cost()

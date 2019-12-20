### 多个函数间的配合
## 变量的作用域
rent = 3000

variable_cost = 0


def cost():
    global variable_cost  # 使用全局的变量
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本费用是' + str(variable_cost))


def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))


cost()
sum_cost()

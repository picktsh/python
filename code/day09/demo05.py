# 作用域练习
quantity = 0


def egg():
    global quantity
    quantity = 108


egg()
print(quantity)


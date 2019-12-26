# 合并两个数组,并排序后输出 基础方案
# list1 = [91, 95, 97, 99]
# list2 = [92, 93, 96, 98]
# merge = list1 + list2  # 合并两个数组
# merge.sort()  # 改变原数组,返回值 None
# print('合并后排序: ', end='')
# print(merge)

# 合并两个数组,并排序后输出 基础方案 sort
list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
merge = list1 + list2  # 合并两个数组
merge.sort()  # 改变原数组,返回值 None
print('合并后: ', end='')  # 结束位置不换行 \n
print(sorted(merge))

list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]
list3 = list1 + list2  # 拼接两个列表
print('排序前的list3', list3)
list3.sort()  # 使用 Python 提供的排序API
print('排序后的list3', list3)
list3.sort(reverse=True)  # 支持参数;可以倒序,传入自定义方法还可以乱序
print('排序前的list3,倒序', list3)
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

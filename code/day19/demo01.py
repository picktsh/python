import csv

with open('assets.csv', 'a', newline='', encoding='utf-8') as csvfile:
    # 调用open()函数打开csv文件，传入参数：文件名“assets.csv”，、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header = ['小区名称', '地址', '建筑时间', '楼栋', '单元', '门牌', '朝向', '面积']
    # 用writerow()函数将表头写进csv文件
    writer.writerow(header)

"""
我们一步步来看，首先我们来把第一对键值对 301:['南北',70] 放进字典start_floor_rooms里，这是我们之前反复接触过的，你可以先看代码和注释。
"""
start_floor = input('请输入起始楼层：')
# end_floor = input('请输入终止楼层：')

# 确定每一单元有几层楼

start_floor_rooms = {}
# 创建字典，存放起始楼层所有户室的信息
floor_last_number = []
# 创建列表，存放户室的尾号如['01','02','03']，后续楼层可复用

last_number = input('请输入起始楼层户室的尾号:（如01，02）')

floor_last_number.append(last_number)
# 将元素添加到存放户室尾号的列表里，如floor_last_number = ['01']

room_number = int(start_floor + last_number)
# 户室名为room_number,由楼层start_floor和尾号last_number组成,如'301'

direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number))
# 输入中文比输入数字要麻烦许多，我们可以先用1和2代替

area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))

start_floor_rooms[room_number] = [direction, area]
# 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}

print(start_floor_rooms)

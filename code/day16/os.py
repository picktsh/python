import os

path = '../'
os.getcwd()  # 返回当前工作目录
os.listdir(path)  # 返回path指定的文件夹包含的文件或文件夹的名字的列表
os.mkdir(path)  # 创建文件夹
os.path.abspath(path)  # 返回绝对路径
os.path.basename(path)  # 返回文件名
os.path.isfile(path)  # 判断路径是否为文件
os.path.isdir(path)  # 判断路径是否为目录

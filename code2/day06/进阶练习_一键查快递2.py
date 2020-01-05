import requests

# name=input('请输入您要查询的快递公司：（用拼音表示）')
num = input('请输入您要查询的快递单号：')
res = requests.get('https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={}'.format(num))
html = res.json()
name = html['auto'][0]['comCode']
check = input('您要查找的是{}吗？(y/n)'.format(name))
if check == 'y':
    res = requests.get(
        'https://www.kuaidi100.com/query?type={}&postid={}&temp=0.8606797497352612&phone='.format(name, num))
    html = res.json()
    item = html['data']
    for i in range(len(item)):
        print(item[i]['time'], end='\t')
        print(item[i]['context'])
"""
————————————————
版权声明：本文为CSDN博主「我是蓝银草」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Crystal_LYP/article/details/99715569
"""

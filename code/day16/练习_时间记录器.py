"""
1 练习介绍

练习目标
我们会通过今天的作业，了解Python的一个内置模块“time模块”的更多用法。

练习要求
在课堂上，我们见过了同样是内置模块的“csv模块”在数据处理方面的强大之处。
而这个练习，我们会和我们的老朋友“time模块”打交道，了解它的更多用法。
下面会先看一个没用模块的“时间记录器”，再借两个网址的知识，对其升级。
"""
"""
2 一个没用模块的“时间记录器”

请运行右侧的代码，并读懂代码中的每一行。
涉及知识：判断、循环、文件读写等。
注：新建文件，在“步骤”旁的“文件”里查看。
"""

#  不用 time模块 的时间记录器。
"""
input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：' % (task_name, task_time))
    task_status = input('请在任务完成后按输入y:')
    actual_time = input('该任务实际用时为几分钟？')
    
    if task_status == 'y':
        with open('timelog1.txt', 'a', encoding='utf-8') as f:  # 将时间日志文档和代码放一起。
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')
"""
"""
3 为“时间记录器”加上time模块

只要我们想通过编程做到更多的事，就避不开主动了解更多知识。
所以，这次的练习，想将主动权更多地交在大家手里。
请你通过搜索和自学，了解并运用下面两个新知识：
time模块中的时间戳（可进行日期运算）和格式化日期（可将日期转换成平常我们所见的格式）；
倒计时的功能怎么用print()函数实现，属于之前没有讲过的方法，需要去搜索新的知识。
"""
# 第一行：必不可少的调用模块。
import time

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：'%(task_name,task_time))
    # 下面应该要有两行代码，自动记录可以计算以及可以打印的开始时间。

    # 这里可以加一个倒计时，实时显示还剩多少时间，可参考左侧提供的资料。代码量大概有5行。

    time_start = time.strftime('%Y/%m/%d %H:%M:%S')
    print('自动记录开始时间为{}'.format(time_start))

    task_time_s = task_time * 60
    while task_time_s:
        print('离结束还剩{}秒'.format(task_time_s))
        time.sleep(1)
        task_time_s -= 1

    task_status = input('请在任务完成后按输入y:')
    actual_time = input('该任务实际用时为几分钟？')
    if task_status == 'y':
        # 下面应该要有两行代码，自动记录可以计算以及可以打印的结束时间。
        # 有了自动记录的始末时间后，记录的代码也需要随之改变。
        with open('timelog2.txt','a', encoding = 'utf-8') as f:
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')

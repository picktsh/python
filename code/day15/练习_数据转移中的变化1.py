"""
1练习介绍

练习目标
我们会通过今天的作业，复习课堂上学到的知识：编码和解码以及文件读写。

练习要求
今天的练习包含3个小练习。
练习1：主要是想要你自己来动手操作一下编码和解码；
练习2：尝试一下图片的读写；
练习3：完成文件转移之间的数据处理，让数据发生变化。
"""
"""
步骤讲解
明确目标很重要（所以重复三遍）。
做到后面的步骤，可再点开左侧的“练习介绍”查看。
"""
"""
2.练习1：编码和解码

请你根据代码中的要求，一步一步完成。
"""
# 1.分别使用gbk和utf-8编码自己的名字，并将其打印出来。
print('唐诗洪'.encode('gbk'))  # b'\xcc\xc6\xca\xab\xba\xe9'
print('唐诗洪'.encode('utf-8'))  # b'\xe5\x94\x90\xe8\xaf\x97\xe6\xb4\xaa'

# 2.复制上一步得到的结果，进行解码，打印出你的名字（两次）。
print(b'\xcc\xc6\xca\xab\xba\xe9'.decode('gbk'))  # 唐诗洪
print(b'\xe5\x94\x90\xe8\xaf\x97\xe6\xb4\xaa'.decode('utf-8'))  # 唐诗洪

# 3.使用gbk解码：b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'，并打印出来。
print(b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'.decode('gbk'))

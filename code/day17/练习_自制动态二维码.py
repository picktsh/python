"""
1 练习介绍

练习目标
我们会通过今天的作业，学习一个新的模块：MyQR，制作一个动态二维码。

练习要求
在昨天的练习里，你已经可以通过自己的学习，完成代码的升级。
所以，今天我们不妨多做些新的尝试。
这次的练习，没有提示，没有准备好的网址。
需求很明确：请你在本地编辑器（如vscode、Pycharm），用 Python 制作一个动态二维码。
所以，请你运用在课堂上看到的提示和知识，去思考，去搜索，去学习，完成今天的练习。
"""
"""
步骤讲解
不用担心，这个模块并不难。
这一个步骤你可以给自己制定一个目标：
读懂一个用 Python 制作动态二维码的代码。
"""
"""
2 代码实操

你应该已经知道了这个模块是：MyQR，也能读懂相关的代码。
请你自学相关模块知识后，自行下载一个gif，然后在本地编辑器（如vscode、Pycharm）完成代码吧。
因为系统里无法展示最后的动态二维码，当你在本地编辑器完成代码并运行成功后，直接点击右侧的运行进入下一步即可。
对了，不要忘了先安装myqr模块，Windows终端里运行'pip install myqr'，Mac终端运行'pip3 install myqr'
"""
# 第一版,普通二维码
# 参考文章: https://github.com/sylnsfar/qrcode/blob/master/README-cn.md
'''from MyQR import myqr
import os

# 这里是二维码的内容
words = 'https://yigeqd.com/'

version, level, qr_name = myqr.run(
    words,  # 扫描二维码后，显示的内容，或是跳转的链接
    version=1,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture=None,  # 图片所在目录，可以是动图 ,'***.gif'
    colorized=False,  # 黑白(False)还是彩色(True)
    contrast=1.0,   # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name=None,   # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_dir=os.getcwd()   # 控制输出文件的路径
)'''
# 接下来就可以修改参数了，colorized改为True就会生成彩图，words替换为链接或者文本


"""
4. 参考代码
"""

# 先导入模块
from MyQR import myqr

myqr.run(
    words='http://weixin.qq.com/r/kzlje9TEE4lsrZAY92yB',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture=None,  # 图片所在目录，可以是动图 ,'she.gif'
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='Python.gif',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
)

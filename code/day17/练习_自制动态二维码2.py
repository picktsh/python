# 第二版,普通二维码
# 参考文章: https://github.com/sylnsfar/qrcode/blob/master/README-cn.md
from MyQR import myqr
import os

# 这里是二维码的内容
# words = 'https://yigeqd.com/'
words = 'https://yigeqd.com/pre/jiangjiang/'
# words = 'https://u.wechat.com/MADTGNZmWW6W5l2eImp43aE'
# 这是图片
# picture = './qrcode/TangSH-B.png'
# picture = './qrcode/fengche.gif'
picture = './qrcode/jiangjiang.gif'

version, level, qr_name = myqr.run(
    words,
    version=5,
    level='H',
    picture=picture,
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
)
# 接下来就可以修改参数了，colorized 改为 True 就会生成彩图，words替换为链接或者文本
print(version)
print(level)
print(qr_name)

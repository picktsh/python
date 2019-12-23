# 代码实操：一次性说完
# 现在，请你趁热打铁，在右侧的代码中新建一个方法，在这个方法中调用实例方法born和live。
# 新建一个方法，让实例只要调用一个方法，就能打印出两个信息。
# 代码完成后，请运行一下，验证是否成功。
class Chinese:
    
    def __init__(self, hometown, region):
        self.hometown = hometown
        self.region = region
        print('程序持续更新中……')
    
    def born(self):
        print('我生在%s。' % (self.hometown))
    
    def live(self):
        print('我在%s。' % (self.region))
    
    def run(self):
        self.born()
        self.live()


my_c = Chinese('中国', '中国大陆')
my_c.run()


# 参考代码
class Chinese:
    
    def __init__(self, hometown, region):
        self.hometown = hometown
        self.region = region
        print('程序持续更新中……')
    
    def born(self):
        print('我生在%s。' % (self.hometown))
    
    def live(self):
        print('我在%s。' % (self.region))
    
    # 新建方法，调用上面的两个方法（注：方法名可自定义）。
    def citys(self):
        self.born()
        self.live()


wufeng = Chinese('广东', '深圳')
wufeng.citys()
# 调用方法后，程序运行方法中的代码（即依次调用方法`born`和`live`）。

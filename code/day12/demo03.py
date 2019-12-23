class Chinese:
    def __init__(self, birth):
        self.hometown = birth
    
    def born(self):
        print('我出生在%s。' % self.hometown)


wufeng = Chinese('广东')
wufeng.born()

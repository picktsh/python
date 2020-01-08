"""
课堂练习
改写下方代码，实现：写一个次数不超过5的循环，每次循环去更改`pagenum`的值，爬取好多好多评论的信息。

不懂做？点击下面的“需要帮助”。
"""
import requests

for i in range(1, 6):
    # 引用requests模块
    res_comments = requests.get(
        'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum={}&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010'.format(
            i))
    # 调用get方法，下载评论列表
    json_comments = res_comments.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_comments = json_comments['comment']['commentlist']
    # 一层一层地取字典，获取评论列表
    for comment in list_comments:
        # list_comments是一个列表，comment是它里面的元素
        print(comment['rootcommentcontent'], end="\n\n")
        # 输出评论
    print('第{}页-----------------------------------'.format(i))
    # 将分页的评论分隔开来

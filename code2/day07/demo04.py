"""
我们的循环会设置为爬两页数据就停止。代码如下：
"""
import requests

# 使用headers是一种习惯
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 建立一个空列表，以待写入数据
articlelist = []
# 设置offset的起始值为第一页的值：10
offset = 10

while True:
    # 封装参数
    params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': str(offset),
        'limit': '10',
        'sort_by': 'voteups',
    }
    # 发送请求，并把响应内容赋值到变量res里面
    res = requests.get(url, headers=headers, params=params)
    # 确认这个response对象状态正确
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        # 用json()方法去解析response对象
        articles = res.json()
        # 定位数据
        data = articles['data']
        
        for i in data:
            # 把数据封装成列表
            list1 = [i['title'], i['url'], i['excerpt']]
            articlelist.append(list1)
            # 在while循环内部，offset的值每次增加20
        offset = offset + 20
        if offset > 30:
            break
        # 如果offset大于30，即爬了两页，就停止
        # ——————另一种思路实现————————————————
        # 如果键is_end所对应的值是True，就结束while循环。
        # if articles['paging']['is_end'] == True:
        # break
        # ————————————————————————————————————
# 打印看看
print(articlelist)

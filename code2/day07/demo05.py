"""
课堂练习
我们的目标：续写代码，请把获取到的两页的文章标题、链接、摘要这些数据，使用csv保存到本地。
"""
import requests
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
articlelist = []
# 建立一个空列表，以待写入数据
offset = 0
# 设置offset的起始值为0
while True:
    params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': str(offset),
        'limit': '20',
        'sort_by': 'voteups',
    }
    # 封装参数
    res = requests.get(url, headers=headers, params=params)
    # 发送请求，并把响应内容赋值到变量res里面
    articles = res.json()
    # print(articles)
    data = articles['data']
    # 定位数据
    for i in data:
        list1 = [i['title'], i['url'], i['excerpt']]
        # 把数据封装成列表
        articlelist.append(list1)
    offset = offset + 20
    # 在while循环内部，offset的值每次增加20
    if offset > 40:
        break
    # 如果offset大于40，即爬了两页，就停止
    # if articles['paging']['is_end'] == True:
    # 如果键is_end所对应的值是True，就结束while循环。
    # break
print(articlelist)
# 打印看看


csv_file = open('demo.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['标题', '链接', '摘要'])
# 最后输出到csv中,获取数据和储存数据分开
for i in articlelist:
    writer.writerow(i)
csv_file.close()
# 储存完毕关闭文档

# 引入requests
import requests

# 封装headers
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 写入网址
url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 封装参数
params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
    'offset': '10',
    'limit': '10',
    'sort_by': 'voteups',
}
# 发送请求，并把响应内容赋值到变量res里面
res = requests.get(url, headers=headers, params=params)
# 确认请求成功，即这个response对象状态正确
print(res.status_code)
# 用json()方法解析response对象，并赋值给变量articles
articles = res.json()
# 打印这个json文件
print(articles)
# 取出键为data的值
data = articles['data']

# 遍历列表，拿到的是列表里的每一个元素，这些元素都是字典，再通过键把值取出来
for i in data:
    print(i['title'])
    print(i['url'])
    print(i['excerpt'])

"""
课堂练习
获取数据：张佳玮知乎文章的页面是：https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes，

然后请你找到标题数据所在的请求页面的Request URL，再用requests.get()方法获取

不懂做？请点击下面的“需要帮助”。
"""
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
# 确认请求成功
print(res.status_code)

"""
练习介绍
我们对关卡内的代码进行修改，实现爬取周杰伦前五页歌曲的歌词
"""
"""
1. 第一步：分析问题，明确目标

需求就是把关卡内的代码稍作修改，将周杰伦前五页歌曲的歌词都爬取下来，结果就是全部展示打印出来。
"""
"""
步骤讲解
需求就是把关卡内的代码稍作修改，将周杰伦前五页歌曲的歌词都爬取下来，结果就是全部展示打印出来。

来，回忆一下，复习本关卡所学知识点的最后一组代码，请认真阅读：
"""
import requests

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
# 这是请求歌曲评论的url
headers = {
    'origin': 'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
}
params = {
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '102065756',
    'cmd': '8',
    'needcommentcrit': '0',
    'pagenum': 0,
    'pagesize': '25',
    'lasthotcommentid': '',
    'domain': 'qq.com',
    'ct': '24',
    'cv': '101010  '
}

res_music = requests.get(url, headers=headers, params=params)
# 发起请求
"""
第二步：写代码

如果没有思路，可以偷偷看下提示哦～
"""
# print(res_music.text)
# 暂存到文件中共方便查看
with open('./res_music.json', 'w', encoding='utf-8') as f:
    f.write(res_music.text)
    f.flush()
# print(res_music.json())
commentlist = res_music.json()['hot_comment']['commentlist']
for i in commentlist:
    print("网友 {} 说: {}".format(i['nick'], i['rootcommentcontent']))

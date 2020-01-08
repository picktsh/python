"""
课堂练习
续写下方代码，使它能够提取20个周杰伦的歌曲名。

不懂做？点击下面的“需要帮助”。
"""
# 引用requests库
import requests

# 调用get方法，下载这个字典
res_music = requests.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 使用json()方法，将response对象，转为列表/字典
json_music = res_music.json()
print(len(json_music))
# print(json_music)
for i in json_music['data']['song']['list']:
    print(i)

"""
参考代码
"""
# 引用requests库
import requests

# 调用get方法，下载这个字典
res_music = requests.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 使用json()方法，将response对象，转为列表/字典
json_music = res_music.json()
# 一层一层地取字典，获取歌单列表
list_music = json_music['data']['song']['list']
# list_music是一个列表，music是它里面的元素
for music in list_music:
    # 以name为键，查找歌曲名
    print(music['name'])

"""
根据前两关所学的知识，如果不出意外，我们的代码大概可以写成这幅模样：
"""
import requests
from bs4 import BeautifulSoup

# 请求html，得到response
res_music = requests.get(
    'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')
# 解析html
bs_music = BeautifulSoup(res_music.text, 'html.parser')
# 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
list_music = bs_music.find_all('a', class_='js_song')
# 对查找的结果执行循环
for music in list_music:
    # 打印出我们想要的音乐名
    print(music['title'])

"""
程序运行的结果，是什么都找不到……当我们写代码遇到这种情况，我们首先要确认自己的代码是否有问题。

我们可以从下往上，倒推着一步一步排查：看提取是不是出错，看解析是不是出错，看请求是不是出错。现在，我们先去print(list_music)看看它里面的值。请点击运行下方代码：
"""
import requests
from bs4 import BeautifulSoup

# 请求html，得到response
res_music = requests.get(
    'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')
# 解析html
bs_music = BeautifulSoup(res_music.text, 'html.parser')
# 查找class属性值为“js_song”的a标签，得到一个由标签组成的列表
list_music = bs_music.find_all('a', class_='js_song')
# 打印它
print(list_music)

"""
list_music，空无一物，它是一个空列表。解析不太可能出问题，因为就一行代码而且符合规范。难道说请求本身就错误了，网页源代码中，根本没有我们要找的歌曲名？我们来print(res_music)。
"""
import requests
from bs4 import BeautifulSoup

# 请求html，得到response
res_music = requests.get(
    'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')
# 打印它
print(res_music.text)

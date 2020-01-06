"""
课堂练习
请你在上一关代码的基础上，把歌曲名、所属专辑、播放时长和播放链接做赋值操作，以及添加存储数据的代码。
"""
import requests, openpyxl

# 创建工作薄
wb = openpyxl.Workbook()
# 获取工作薄的活动表
sheet = wb.active
# 工作表重命名
sheet.title = 'lyrics'

sheet['A1'] = '歌曲名'  # 加表头，给A1单元格赋值
sheet['B1'] = '所属专辑'  # 加表头，给B1单元格赋值
sheet['C1'] = '播放时长'  # 加表头，给C1单元格赋值
sheet['D1'] = '播放链接'  # 加表头，给D1单元格赋值

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    
    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        name = music['name']
        # 查找专辑名，把专辑名赋给album
        album = music['album']['name']
        # 查找播放时长，把时长赋值给time
        time = music['interval']
        # 查找播放链接，把链接赋值给link
        link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        sheet.append([name, album, time, link])
        print('歌曲名：' + name + '\n' + '所属专辑:' + album + '\n' + '播放时长:' + str(time) + '\n' + '播放链接:' + link)
# 最后保存并命名这个Excel文件
wb.save('JayZhou.xlsx')

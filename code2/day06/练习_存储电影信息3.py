"""
第四步：另辟蹊径，用csv格式存储信息

思考下如何用csv创建写入存储呢？

请修改下方代码，实现使用csv存储信息。
"""
import requests, bs4, csv

csv_file = open('top250.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(csv_file)
write.writerow(['序号', '电影名', '评分', '推荐语', '链接'])

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    if bs == None:
        break
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']
        
        if titles.find('span', class_="inq") != None:
            tes = titles.find('span', class_="inq").text
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)
            write.writerow([num, title, comment, tes, url_movie])
        else:
            print(num + '.' + title + '——' + comment + '\n' + '\n' + url_movie)
            write.writerow([num, title, comment, '', url_movie])

csv_file.close()
print('程序结束')

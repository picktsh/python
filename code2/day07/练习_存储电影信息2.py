"""
第三步： 完善代码，用Excel存储信息
要存储在Excel中呢，需要先创建工作表，重命名，再设置表头，把爬取的信息写成列表，然后用append函数多行写入Excel，最后命名保存这个Excel 文件。
请改写下方的爬虫代码，实现使用Excel存储信息。
"""
import requests, bs4, openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'top250'
sheet.append(['序号', '电影名', '评分', '推荐语', '链接'])

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
            sheet.append([num, title, comment, tes, url_movie])
        else:
            print(num + '.' + title + '——' + comment + '\n' + '\n' + url_movie)
            sheet.append([num, title, comment, '', url_movie])

wb.save('top250.xlsx')
print('程序结束')

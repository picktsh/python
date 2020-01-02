import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

classList = soup.select("#main.site-main .type-post")

print(len(classList))

for i in classList:
    title = i.select_one(".entry-title").text
    date = i.select_one(".entry-meta .entry-date").text
    href = i.select_one(".entry-title a")['href']
    print("标题:{},日期:{},链接:{}".format(title, date, href))

print("程序结束")

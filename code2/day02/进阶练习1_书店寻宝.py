import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

classList = soup.select(".side_categories .nav-list>li>ul>li")

print(len(classList))

for i in classList:
    item = i.select_one("a").text.replace("\n", "").replace("\t", "")
    print(item)

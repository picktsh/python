import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

classList = soup.select(".page_inner .row section ol.row .col-lg-3")

print(len(classList))

for i in classList:
    bookName = i.select_one("h3 a").text
    bookStar = len(i.select_one(".star-rating .icon-star"))
    bookPrice = i.select_one(".product_price .price_color").text
    print("书名:{},评分:{},价格:{}".format(bookStar, bookName, bookPrice))

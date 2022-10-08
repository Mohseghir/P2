#on choisi la category sequentiel-art

import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#recuperer les lien d'une page
h3s = soup.findAll("h3")
url_book_list = []
page_url = []
urls_category = []
for h3 in h3s:
    link = h3.find("a")["href"].replace("../../..", "http://books.toscrape.com/catalogue")
    url_book_list.append(link)
print(url_book_list)
print(len(url_book_list))
#cas de plusieur pages
if len(url_book_list) == 20: #on cherche "next"
    next_page = soup.find('ul', 'pager').find('li', 'next')
    page_number = 1
    while next_page:


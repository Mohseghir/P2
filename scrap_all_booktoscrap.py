import requests
from bs4 import BeautifulSoup
from scrap_one_category import all_category_list

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# trouver la liste de toutes les catégorie
all_category_list_list = []
lis = soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
for li in lis:
    link = url + li.find("a")["href"]
    all_category_list_list.append(link)
print(all_category_list_list)
# exploiter la fonction all_category_list pour extraire les infos et les images de tout les livres
all_website_book_list = []
for url_category in all_category_list_list:
    category_book_list = all_category_list(url_category)
    all_website_book_list.append(category_book_list)
# print(all_website_book_list)

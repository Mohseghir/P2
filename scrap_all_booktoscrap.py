import csv
import requests
from bs4 import BeautifulSoup
from scrap_one_category import all_category_list
from scrap_one_book import book_info

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

all_category_list_list = []
lis = soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
for li in lis:
    link = url + li.find("a")["href"]
    all_category_list_list.append(link)
# print(all_category_list_list)


all_website_book_list = []
for url_category in all_category_list_list:
    category_book_list = all_category_list(url_category)
    all_website_book_list.append(category_book_list)
# print(all_website_book_list)
# regrouper tout les liens dans une seule liste et non pas en plusieur array
all_website_book_list_list = []
for array in all_website_book_list:
    for arrayj in array:
        all_website_book_list_list.append(arrayj)
print(all_website_book_list_list)

with open('all_booktoscrap_infos.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    en_tete = ['product_page_url', 'UPC', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
               'product_description', 'category', 'review_rating', 'image_url']
    writer.writerow(en_tete)
    for lien_book in all_website_book_list_list:
        csv_allbooks_data = book_info(lien_book)
        writer.writerow(
            [csv_allbooks_data[0], csv_allbooks_data[1], csv_allbooks_data[2], csv_allbooks_data[3],
             csv_allbooks_data[4],
             csv_allbooks_data[5], csv_allbooks_data[6], csv_allbooks_data[7],
             csv_allbooks_data[8], csv_allbooks_data[9]])
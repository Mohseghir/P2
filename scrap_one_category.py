# on choisi la category sequentiel-art
import csv
import requests
from bs4 import BeautifulSoup
from scrap_one_book import book_info

url = 'https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


# def une fonction pour extraire les liens d'une seule page
def book_list(soup):
    url_book_list = []
    h3s = soup.findAll("h3")
    for h3 in h3s:
        link = h3.find("a")["href"].replace("../../..", "http://books.toscrape.com/catalogue")
        url_book_list.append(link)
    return url_book_list


url_book_list = book_list(soup)
print(url_book_list)
print(len(url_book_list))


# def de la fonction qui etend le chargement des listes sur toute les pages de une categorie
def all_category_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    url_book_list = book_list(soup)
    if len(url_book_list) == 20:
        page_next = soup.find("ul", "pager").find("li", "next")
        page_number = 1
        while page_next:
            page_number += 1
            page_url = url.replace("index.html", f"page-{page_number}.html")
            page = requests.get(page_url)
            soup = BeautifulSoup(page.content, 'html.parser')
            url_book_list.extend(book_list(soup))
            page_next = soup.find("ul", "pager").find("li", "next")
    return url_book_list


url_book_list = all_category_list(url)
print(url_book_list)

with open('one_category_infos.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    en_tete = ['product_page_url', 'UPC', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
               'product_description', 'category', 'review_rating', 'image_url']
    writer.writerow(en_tete)
    for urls in url_book_list:
        csv_books_data = book_info(urls)
        writer.writerow(
            [csv_books_data[0], csv_books_data[1], csv_books_data[2], csv_books_data[3], csv_books_data[4],
             csv_books_data[5], csv_books_data[6], csv_books_data[7],
             csv_books_data[8], csv_books_data[9]])
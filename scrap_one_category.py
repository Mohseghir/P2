# on choisi la category sequentiel-art
import csv
import requests
from bs4 import BeautifulSoup
from scrap_one_book import book_info

url = 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# recuperer les lien d'une page
page_url = []
urls_category = []
urls = []


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




with open('book_infos.csv', 'w') as csv_file:
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

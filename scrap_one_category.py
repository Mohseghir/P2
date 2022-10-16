import csv
import requests
from bs4 import BeautifulSoup
from scrap_one_book import book_info
import pathlib

url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
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


# def de la fonction qui etend le chargement des listes sur toute les pages de une categorie
def all_category_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    url_book_list = book_list(soup)
    title_category = soup.find('h1').text
    print(title_category)
    new_dir_name = title_category
    category_name = title_category + ".csv"
    new_dir = pathlib.Path('./data/', new_dir_name)
    new_image_dir = pathlib.Path('./data/', new_dir_name, 'images')
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
    # exploiter la generation des lien pour integer les résultats dans des dossiers au fur et à mesure de l'avancement du code
    new_dir.mkdir(parents=True, exist_ok=True)
    new_image_dir.mkdir(parents=True, exist_ok=True)
    with open(new_dir / category_name, 'w') as csv_file:
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
            img_data = requests.get(csv_books_data[9]).content
            # certain titre de livre contients '/' ce qui pose problème avec les paths
            image_name = csv_books_data[2].replace('/', '-') + ".png"
            with open(new_image_dir / image_name, 'wb') as handler:
                handler.write(img_data)
    return url_book_list


url_book_list = all_category_list(url)

# print(len(url_book_list))

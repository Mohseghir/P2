import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html'


def book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text.encode('utf8').decode('ascii', 'ignore'), 'html.parser')
    all_infos = soup.find_all("td")
    infos = []
    for info in all_infos:
        infos.append(info.string)
    # avoir toutes les infos pour un livre
    product_page_url = url
    upc = infos[0]
    title = soup.find('article').h1.text
    price_excluding_tax = infos[2]
    price_including_tax = infos[3]
    number_available = infos[5]
    review_rating = infos[6]
    # suite à la remarque que certains livres n'ont pas de description
    descrip = soup.find('article').find('p', recursive=False)
    if descrip is not None:
        product_description = descrip.text
    else:
        product_description = None

    category = soup.find_all("a")[3].text
    main_url = 'http://books.toscrape.com/'
    image_url = soup.find('img')['src'].replace('../../', main_url)
    return product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url


# création du fichier CSV avec toutes les infos en entête

en_tete = ['product_page_url', 'UPC', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
           'product_description', 'category', 'review_rating', 'image_url']
with open('book_infos.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    csv_data = book_info(url)
    writer.writerow(
        [csv_data[0], csv_data[1], csv_data[2], csv_data[3], csv_data[4], csv_data[5], csv_data[6], csv_data[7],
         csv_data[8], csv_data[9]])

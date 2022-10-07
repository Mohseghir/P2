import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

print(url)

soup = BeautifulSoup(response.text, 'html.parser')

all_infos = soup.find_all("td")
infos = []
for info in all_infos:
    infos.append(info.string)
print(infos) #avoir toutes les info pour un livre

UPC = infos[0]
print(UPC)
title = soup.find('article').h1.text
print(title)
product_description = soup.find('article').find('p', recursive = False).text #recursive=false renvoir le premier 'child' qui s'appel 'p' dans article
#print(product_description)

price_excluding_tax = infos[2]
print(price_excluding_tax)

price_including_tax = infos[3]
print(price_including_tax)

number_available = infos[5]
print(number_available)

category = soup.find_all("a")[3].text #sortir le 4eme "a" trouvé
print(category)

review_rating = infos[6]
print(review_rating)

main_url = 'http://books.toscrape.com/'
image_url = soup.find('img')['src'].replace('../../', main_url)
print(image_url)

# creation du fichier CSV avec toutes les info en entete
en_tete = ['product_page_url', 'UPC', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
with open('book_infos.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    writer.writerow([url, UPC, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url])

# (à utiliser plus tard ) zip permet d'itérer sur plusieure liste listes à la fois
#for url, UPC, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url in zip(url,UPC, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url):

""""



image_url = infos[]


for tr in trs:
	a = tr.find('td.str')
	info = str('a')
print(info)

Objectif du projet : suivre les prix des livre sur : Books to scrape

1ere étape, choisir la page d'un seul produit et
créer un fichier csv qui a comme en-tête:
# product_page_url
# universal_ product_code (upc)
# title
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url

# j'importe requests et bs4
#universal_ product_code = soup.find_all("UPC", class_="table table-striped")
#print(niversal_ product_code)


2-faire la meme chose pour une catégorie de livre 

remarque : plusieurs page dans une mm cathégorie 

3-appliquer le meme travail sur l'ensemble du site 

ecrire un fichier csv pour chaque catégorie 

4- téléchanrger et enregisrter le fichier image de chaque page produit consultée

5-enregistrer le travails sur un GitHub + commits avec des messages de commits (pour chaque etape par exemple)

6- enregisrter un fichier requirements.txt (sans l'environement retuel et sans les csv)
7- ecrire un README.md

Python 
"""


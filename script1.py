import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)

print(url)

soup = BeautifulSoup(response.text, 'html.parser')

#trs = soup.findAll('tr')
#[print(str(tr) + '\n' ) for tr in trs]
"""
tds = soup.findAll('td')
for td in tds:
	a = str(td)
	for a in range(4, -5):
		print(a) 
"""
titres_bs = soup.find_all("td")
titres = []
for titre in titres_bs:
    titres.append(titre.string)
print(titres[3])
"""
for tr in trs:
	a = tr.find('td.str')
	info = str('a')
print(info)
"""

"""
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
"""
# j'importe requests et bs4
#universal_ product_code = soup.find_all("UPC", class_="table table-striped")
#print(niversal_ product_code)

"""
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


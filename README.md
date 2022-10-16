# P2
web scraping

Programme d'extraction des prix du site http://books.toscrape.com/ avec Python

# Exploitation du programme:

Pour utiliser l'outil il vous faut :

- Python 3.10 depuis https://www.python.org/
- Git
- un compte Github.


Installation

Téléchargez le repository en utilisant la commande suivante : git clone https://https://github.com/Mohseghir/P2

Positionnez-vous dans le dossier : P2

Activez l'environnement virtuel en utilisant :

`python3 -m venv env`

`source env/bin/activate`

Installez les modules nécessaires en utilisant :

`pip3 install -r requirements.txt`

Execution: 


Lancez la commande : `python3 scrap_all_booktoscrap.py` depuis votre terminal. (pour Windows utilisez `py scrap_all_booktoscrap.py`)

Output:


A la fin du processus, un dossier "data" sera crée avec un sous-dossier par catégorie. 

Ce dernier contient le fichier csv de la catégorie, ainsi qu'un dossier images avec les images de tous les livres de la dite catégorie.
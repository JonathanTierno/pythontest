import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://www.danston.com"
    response = requests.get(url)
    content = response.content
    
    # Crear un objeto BeautifulSoup con el contenido HTML de la página de listado de artículos
    soup = BeautifulSoup(driver.content, 'html.parser')

    # Encontrar todos los elementos de artículo en la página
    article_elements = soup.find_all('div', class_='prod_item')

    # Iterar sobre los elementos de artículo y extraer la información deseada
    for article in article_elements:
        name = article.find('span', itemprop = 'itemprop').text
        sku = article.find('span', itemprop = 'sku').text
        price = article.find('span', itemprop = 'pprecio').text

        print('Nombre:', name)
        print('SKU:', sku)
        print('Precio:', price)
        print('---')

from bs4 import BeautifulSoup
import requests
import pandas as pd
from xml.etree import ElementTree

urls = ['https://e00-marca.uecdn.es/rss/portada.xml','https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/deportes/portada','https://e00-elmundo.uecdn.es/elmundodeporte/rss/portada.xml']

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'xml', from_encoding='utf-8')
    #dicCategorias={dato['title'] : dato.getText() for dato in soup.find_all('item')}
    for dato in soup.find_all('item'): 
        sp = BeautifulSoup(dato,'xml',from_encoding='utf-8')
        datosdict = {sp.find('title') : dato.getText() for dato in sp.find_all('category')}
    print(datosdict)
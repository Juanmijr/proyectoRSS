from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import operator
import json

urls = ['https://e00-marca.uecdn.es/rss/portada.xml','https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/deportes/portada','https://e00-elmundo.uecdn.es/elmundodeporte/rss/portada.xml']
listaNoticias=[]
for url in urls:
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'xml', from_encoding='utf-8')
    
    for dato in soup.find_all('item'): 

        #sp = BeautifulSoup(dato,'xml',from_encoding='utf-8')
        listCategorias= []
        for cat in dato.findAll('category'):
            listCategorias.append(cat.getText())
        if (len(dato.pubDate.getText())==31):
            fecha_dt = datetime.strptime(dato.pubDate.getText(), '%a, %d %b %Y %H:%M:%S %z')
        if (len(dato.pubDate.getText())==29):
            fecha_dt = datetime.strptime(dato.pubDate.getText(), '%a, %d %b %Y %H:%M:%S %Z')
        print(fecha_dt)
        listaNoticias.append({'titulo':dato.title.getText(),'fecha':fecha_dt.strftime('%Y-%m-%d'), 'enlace':dato.link.getText(),'categorias':listCategorias})

with open('sinorden.json', 'w') as fp:
    json.dump(listaNoticias, fp)
print('\n HASTA AQUÍ LLEGA ESTO LOCO \n')
listaNoticias.sort(key= operator.itemgetter('fecha'),reverse=True)
with open('ordenado.json', 'w') as fp:
        json.dump(listaNoticias, fp)

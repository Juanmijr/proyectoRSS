from bs4 import BeautifulSoup
import requests
import pandas as pd
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
        listaNoticias.append({'titulo':dato.title.getText(),'fecha':dato.pubDate.getText(), 'enlace':dato.link.getText(),'categorias':listCategorias})

with open('sinorden.json', 'w') as fp:
    json.dump(listaNoticias, fp,ensure_ascii=False)
print('\n HASTA AQUÍ LLEGA ESTO LOCO \n')
listaNoticias.sort(key= operator.itemgetter('fecha'))
with open('ordenado.json', 'w') as fp:
        json.dump(listaNoticias, fp,ensure_ascii=False)

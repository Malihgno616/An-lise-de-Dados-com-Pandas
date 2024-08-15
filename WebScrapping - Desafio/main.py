from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

texto_string = requests.get(' https://globoesporte.globo.com/').text
hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})

print("Quantidade de manchetes = ", len(lista_noticias))

print(lista_noticias[0].contents[1].text.replace('"',""))

print(lista_noticias[0].find('a').get('href'))

descricao = lista_noticias[0].contents[2].text

"""if not descricao:
    descricao = noticia.find('div',attrs={'class': 'bstn-related'})
    descricao = descricao.text if descricao else None
print(descricao)"""    
    

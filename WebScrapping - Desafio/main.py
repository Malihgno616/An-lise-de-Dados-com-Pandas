from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

texto_string = requests.get(' https://globoesporte.globo.com/').text
hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})

lista_noticias = bsp_texto.find_all('div', attrs={'class': 'feed-post-body'})


print("Quantidade de manchetes = ", len(lista_noticias))

print(lista_noticias[0].contents[1].text.replace('"',""))

print(lista_noticias[0].find('a').get('href'))
print()

descricao = lista_noticias[0].contents[2].text

# Acessar e exibir a primeira notícia
if lista_noticias:
    primeira_noticia = lista_noticias[0]
    
    # Exibir o texto da manchete
    manchete = primeira_noticia.find('a').text.strip()
    print(manchete)
    
    # Exibir o link da notícia
    link = primeira_noticia.find('a').get('href')
    print(link)
    
    # Exibir a descrição da notícia
    descricao = primeira_noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    descricao = descricao.text.strip() if descricao else "Descrição não disponível"
    print(descricao)
else:
    print("Nenhuma notícia encontrada.")  
    

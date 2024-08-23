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
    
metadados = lista_noticias[0].find('div', attrs={'class':'feed-post-metadata'})

time_delta = metadados.find('span', attrs={'class':'feed-post-metadata'})
secao = metadados.find('span', attrs={'class':'feed-post-metadata-section'})

time_delta= time_delta.text if time_delta else None
secao = secao.text if secao else None

print('time_delta = ', time_delta)
print('seção = ', secao)


dados = []

for noticia in lista_noticias:
    manchete = noticia.contents[1].text.replace('"',"")
    link = noticia.find('a').get('href')

    descricao = noticia.contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class': 'bstn-related'})
        descricao = descricao.text if descricao else None

    metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None

    dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
df.head()

print(df)
print()

class ExtracaoPortal:
    def __init__(self):
        self.portal = None
    
    def extrair(self, portal):
        self.portal = portal
        texto_string = requests.get('https://globoesporte.globo.com/').text
        hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        bsp_texto = BeautifulSoup(texto_string, 'html.parser')
        lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
        
        dados = []

        for noticia in lista_noticias:
            manchete = noticia.contents[1].text.replace('"',"")
            link = noticia.find('a').get('href')

            descricao = noticia.contents[2].text
            if not descricao:
                descricao = noticia.find('div', attrs={'class': 'bstn-related'})
                descricao = descricao.text if descricao else None

            metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
            time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
            secao = metadados.find('span', attrs={'class': 'feed-post-metadata-section'})

            time_delta = time_delta.text if time_delta else None
            secao = secao.text if secao else None

            dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))

        df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
        return df
    
df = ExtracaoPortal().extrair("https://globoesporte.globo.com/")
df.head()
    
print(df)
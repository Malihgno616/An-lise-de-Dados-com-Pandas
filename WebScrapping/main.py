from datetime import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd

texto_string = requests.get(' https://globoesporte.globo.com/').text
hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_notícias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})

print("Quantidade de manchetes = ", len(lista_notícias))

print(lista_notícias[0].contents[1].text.replace('"',""))


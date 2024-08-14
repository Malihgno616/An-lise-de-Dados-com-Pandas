import pandas as pd #importa a biblioteca Pandas e abreviamos 

#pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
#Utilizando o SERIES 
pd.Series(data=5) 

lista_nomes = 'Joao Felipe Victor Arthur'.split()#O split distribui as strings

pd.Series(lista_nomes) #Cria uma Series com uma lista de nomes

cpfs = '111.111.111 222.222.222 333.333.333 444.444.444'.split()

pd.Series(lista_nomes, index=cpfs)

series_dados = pd.Series(lista_nomes, index=cpfs)

series_dados.loc['111.111.111']

print(series_dados)
    
series_dados = pd.Series([10.2, -1, None, 15, 23,4])

print('Quantidade de linhas = ', series_dados.shape)#retorna o número de linhas
print('Tipos de dados',series_dados.dtypes)#retorna o tipo das variáveis
print('Os valores são únicos?', series_dados.is_unique)#Verifica se os valores são únicos ou não
print('Existem valores nulos? ', series_dados.hasnans)#Verifica se existem valores nulos ou não
print('Quantos valores existem?', series_dados.count())#Conta quantas variaveis existem    

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series   
    
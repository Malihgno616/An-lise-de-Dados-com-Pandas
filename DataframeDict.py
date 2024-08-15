import pandas as pd

#Biblioteca Pandas usando a funcionalidade DataFrame com dicionário

dados = {
    'nome': 'Joao Maria Lucas Arthur'.split(),
    'cpf': '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44'.split(),
    'emails': 'joao@email.com maria@email.com lucas@email.com arthur@email.com'.split(),
    'idade': [23,33,32,19],
}

pd.DataFrame(dados)

df_dados = pd.DataFrame(dados)


print('\nInformações do DataFrame:\n')
print(df_dados.info())#Apresenta informações
print()

print('\nQuantidaed de linhas e colunas = ',df_dados.shape)#mostra a quantidade de linhas
print('\nTipos de Dados\n', df_dados.dtypes)#mostra o tipo de variáveis

print('\nQual o maior valor?\n', df_dados.max()) #Extrai o valor máximo
print('\nQual é o menor valor de cada coluna?\n', df_dados.min())#Extrai o valor mínimo
print('\nQual é a média aritmética?\n', df_dados.select_dtypes(include='number').mean()) # Extrai a média aritmética de cada coluna numérica
print('\nQual é o desvio padrão?\n', df_dados.select_dtypes(include='number').std()) # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', df_dados.select_dtypes(include='number').median())# Extrai a mediana de cada coluna numérica

print('\nResumo\n', df_dados.describe())  # Exibe um resumo
print()
print(df_dados.head()) # Exibe os 5 primeiros registros do DataFrame


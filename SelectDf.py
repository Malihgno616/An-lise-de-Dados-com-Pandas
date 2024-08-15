#SELECIONANDO COLUNAS EM UM DATAFRAME
import pandas as pd

dados = {
    'nome': 'Joao Maria Lucas Arthur'.split(),
    'cpf': '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44'.split(),
    'emails': 'joao@email.com maria@email.com lucas@email.com arthur@email.com'.split(),
    'idade': [23,33,32,19],
}

pd.DataFrame(dados)

df_dados = pd.DataFrame(dados)

#SELECIONA UMA COLUNA DE UM DATAFRAME
df_uma_coluna = df_dados['idade']
print(type(df_uma_coluna))
print(df_uma_coluna)

print()

#SELECIONA DUAS COLUNAS DE UM DATAFRAME
colunas = ['nome', 'cpf']
df_duas_colunas = df_dados[colunas]
print(df_duas_colunas)

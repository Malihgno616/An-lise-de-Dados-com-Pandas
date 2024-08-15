import pandas as pd 
#Importaremos o pandas e usaremos a funcionalidade Dataframe

#pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

lista_nomes = 'Joao Maria Jose Jean'.split()
lista_cpf = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44'.split()
lista_emails = 'joao@email.com maria@email.com jose@email.com jean@email.com'.split()
lista_idades = [22,19,21,24]

nomes = pd.DataFrame(lista_nomes, columns=['NOME'])

print(nomes)

dados = list(zip(lista_nomes, lista_cpf, lista_idades, lista_emails)) # cria uma lista de tuplas

tuplas = pd.DataFrame(dados, columns=['nome', 'cpfs','idade','email'])

print()
print(tuplas)



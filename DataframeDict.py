import pandas as pd

dados = {
    'nomes': 'Joao Maria Lucas Arthur'.split(),
    'cpfs': '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44'.split(),
    'emails': 'joao@email.com maria@email.com lucas@email.com arthur@email.com'.split(),
}

dict = pd.DataFrame(dados)
print()
print(dict)
print()


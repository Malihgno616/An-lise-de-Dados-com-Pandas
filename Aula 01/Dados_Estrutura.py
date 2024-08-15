#LEITURA DE DADOS ESTRUTURADOS COM A BIBLIOTECA PANDAS

#pandas.read_XXXXX()

#pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False, thousands=',', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)

#pandas.read_html()

import pandas as pd

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)
print(df_bancos)
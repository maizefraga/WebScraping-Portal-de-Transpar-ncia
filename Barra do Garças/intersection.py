import pandas as pd

#Criação dos dataframes por arquivo JSON
df1 = pd.read_json('data20.json', orient='records')
df2 = pd.read_json('data21.json', orient='records')
df3 = pd.read_json('data22.json', orient='records')

#Aglutinação dos dataframes
df_js = df1 + df2 + df3

#Criação do dataframe do arquivo com os dados dos servidores
df_map = pd.read_json('map.json')

#Intersecção dos dois dataframes
df_merge = pd.merge(df_map.T, df_js, how='inner', on='nome')

#Printa a intersecção
print(df_merge)

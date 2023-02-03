import pandas as pd

df1 = pd.read_json('data20.json', orient='records')
df2 = pd.read_json('data21.json', orient='records')
df3 = pd.read_json('data22.json', orient='records')

df_js = df1 + df2 + df3

df_map = pd.read_json('map.json')

df_merge = pd.merge(df_map.T, df_js, how='inner', on='nome')
print(df_merge)

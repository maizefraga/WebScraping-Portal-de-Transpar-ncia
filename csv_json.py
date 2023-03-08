import pandas as pd
import json

servidores = f"/home/maizefs/Downloads/projeto_de_pesquisa/scraping_tranparencia/camponovodoparecis.json"


df_servidores = pd.read_json(servidores)

# Salvar os dados dos servidores em um arquivo CSV
df_servidores.to_json("camponovodoparecis.json")


# Carregar os dados dos alunos dos anos 2020 a 2023
urls_alunos = [
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/fc30244a-166d-4830-a66d-a573ebe187eb/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/d2a472aa-3a02-4d45-bc65-5852fa9be664/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/96f114e2-58f9-4f59-9c44-f59814c0b264/download/aluno.csv",
    "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/1535c8e2-f1c4-4dcf-9948-dc734522d040/download/aluno.csv",
]
# cria um lista vazia
df_alunos = []

# __import__('ipdb').set_trace()

# percorre os links e adiociona na lista anterio
for url in urls_alunos:
    df = pd.read_csv(url, encoding="utf-8", sep=",")
    df_alunos.append(df)


# Concatenar os dataframes dos alunos em um único dataframe
df_alunos = pd.concat(df_alunos)
df_alunos['nome'] = df_alunos['nome'].str.upper()
# __import__('ipdb').set_trace()
# Juntar os dataframes dos servidores e dos alunos com base no nome

df_merge = pd.merge(df_servidores.T, df_alunos, how="inner", on='nome')

# apaga os nomes duplicados na lista
df_merge = df_merge.drop_duplicates(subset='nome', keep='first')


print("\n Esses são os alunos que estudaram no IF e agora trabalham para o governo\n")


print(df_merge)

"""
file = open('intersecao.json', 'w')
json.dump(df_merge, file, ensure_ascii=False)
file.close()
"""

import pandas as pd
import csv


# ATRIBUI O LINK DO ARQUIVO EM CSV PARA UMA VARIAVEL
url_servidores = f"https://www.gp.srv.br/transparencia_barradogarcas/servlet/arealizadownload?application%2Fdownload,%2Fopt%2Fglassfish%2Fv4%2Fglassfish%2Fnodes%2Flocalhost-coplan%2FInstCoplan%2Fapplications%2Fapptransparenciabarradogarcas%2FPublicTempStorage%2Fdocumentoc34efda9b821d87f560855429a8d.txt,Documento.csv"
# LER O LINK EM CSV E CRIA UM DATAFRAME
data_servidores = pd.read_csv(url_servidores, encoding='utf-8', sep=';')
# CRIANDO UM ARQUIVO CSV A PARTIR DO DATAFRAME
data_servidores.to_csv('servidores.csv')
print('sv')

# ATRIBUI O LINK DO ARQUIVO EM CSV PARA UMA VARIAVEL
url23 = f'https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/1535c8e2-f1c4-4dcf-9948-dc734522d040/download/aluno.csv'
# LER O LINK EM CSV E CRIA UM DATAFRAME
data23 = pd.read_csv(url23, encoding='utf-8', sep=',')
# CRIANDO UM ARQUIVO CSV A PARTIR DO DATAFRAME
data23.to_csv('data23.csv')
print('23')

# ATRIBUI O LINK DO ARQUIVO EM CSV PARA UMA VARIAVEL
url22 = f'https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/96f114e2-58f9-4f59-9c44-f59814c0b264/download/aluno.csv'
# LER O LINK EM CSV E CRIA UM DATAFRAME
data22 = pd.read_csv(url22, encoding='utf-8', sep=',')
# CRIANDO UM ARQUIVO CSV A PARTIR DO DATAFRAME
data22.to_csv('data22.csv')
print('22')

# ATRIBUI O LINK DO ARQUIVO EM CSV PARA UMA VARIAVEL
url21 = f'https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/d2a472aa-3a02-4d45-bc65-5852fa9be664/download/aluno.csv'
# LER O LINK EM CSV E CRIA UM DATAFRAME
data21 = pd.read_csv(url22, encoding='utf-8', sep=',')
# CRIANDO UM ARQUIVO CSV A PARTIR DO DATAFRAME
data21.to_csv('data21.csv')
print('21')

# ATRIBUI O LINK DO ARQUIVO EM CSV PARA UMA VARIAVEL
url20 = f'https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/fc30244a-166d-4830-a66d-a573ebe187eb/download/aluno.csv'
# LER O LINK EM CSV E CRIA UM DATAFRAME
data20 = pd.read_csv(url22, encoding='utf-8', sep=',')
# CRIANDO UM ARQUIVO CSV A PARTIR DO DATAFRAME
data20.to_csv('data20.csv')
print('20')

# TRANSFORMA OS ARQUIVOS CSV EM DATAFRAME
df20 = pd.read_csv('data20.csv')
df21 = pd.read_csv('data21.csv')
df22 = pd.read_csv('data22.csv')
df23 = pd.read_csv('data23.csv')

# AGLUTINANDO OS DATAFRAMES
df_ifmt = df20 + df21 + df22 + df23
# TRANSFORMA O ARQUIVO CSV DOS SERVIDORES EM DATAFRAME
df_servidores = pd.read_csv('servidores.csv')
# INTERSECÇÃO DOS DATAFRAMES
df_merge = pd.merge(df_servidores, df_ifmt, how='inner',
                    left_on="NOME", right_on="nome")
print(df_merge)

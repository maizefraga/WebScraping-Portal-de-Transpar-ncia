from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from urllib.request import urlopen

#Atribui a url do arquivo JSON a uma variavel
url22 = "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/e33bbded-18d9-46af-bc29-702093ae1347/download/aluno.json"
#Procura um retorno para essa url
response22 = urlopen(url22)
#atribui o valor desse arquivo em uma variável
data22 = json.loads(response22.read())
#Cria um arquivo JSON
file = open('data22.json', 'w')
json.dump(data22, file, ensure_ascii=False)
file.close()

url21 = "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/dd53dca0-d413-4f90-a0ea-c5e12ac77af5/download/aluno.json"
response21 = urlopen(url21)
data21 = json.loads(response21.read())
file = open('data21.json', 'w')
json.dump(data21, file, ensure_ascii=False)
file.close()

url20 = "https://dados.ifmt.edu.br/dataset/6b7c7c38-587a-436b-a7b2-4e3ca59d1ca8/resource/c5917feb-d9d8-4a6f-a00e-6e5d8bff7529/download/aluno.json"
response20 = urlopen(url20)
data20 = json.loads(response20.read())
file = open('data20.json', 'w')
json.dump(data20, file, ensure_ascii=False)
file.close()

import requests
from bs4 import BeautifulSoup
import smtplib
import json
from os import environ

# Configurações do email
remetente = environ['remetente']
senha = environ['remetente']
destinatario = environ['remetente']
headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'


# Produto e valor máximo desejado
produto = 'Galaxy S20 fe'
valor_maximo = 5000


# URL do Google Shopping e  parâmetros da consulta
url = f'https://www.google.com.br/search'
params= {"q": produto, "tbm" : "shop"}

# Faz a requisição da página
response = requests.get("https://www.google.com/search", headers=headers, params=params)

# Faz o parsing do HTML
soup = BeautifulSoup(response.text, "lxml")

# Busca os resultados da pesquisa
results = soup.find_all('div', class_='xcR77')

# Percorre os resultados
for result in results:
    # Extrai o nome e o preço do produto
    nome_element = result.find('div', class_='rgHvZc')
    if nome_element is None:
        continue
    nome = nome_element.text
    preco_element = result.find('span', class_='HRLxBb')#.text
    if preco_element is None:
        continue
    preco_str = preco_element.text
    preco = preco_str.replace('R$', '').replace('.', '').replace(',', '.')
    preco_final = preco.split(' ')[0]
    detalhe_preco = preco.split(' ')[1]
    preco = float(preco_final)
    link = result.find('div', class_='rgHvZc')['href']

    # Verifica se o preço é menor que o valor máximo desejado
    if preco < valor_maximo:
        # Envia o link por e-mail
        link = result.find('a', class_='DKkjqf')['href']
        assunto = f'{nome} por R${preco} - {detalhe_preco}'
        mensagem = f'Link: {link}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, f'Subject: {assunto}\n\n{mensagem}')
        server.quit()
        print(link)
        break


    
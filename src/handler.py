import sys
print(sys.path)

from selenium.webdriver.common.by import By
import time
from services.selenium_services import SeleniumServices
import smtplib
from os import environ
import json


def main():
    # remetente = environ['remetente']
    # senha = environ['senha']
    # destinatario = environ['destinatario']

    produto = 'Galaxy'
    # valor_maximo = 5000000

    selenium = SeleniumServices()

    driver = selenium.start_driver()
    url = f'https://www.zoom.com.br/search?q={produto}'
    # url = f'https://www.google.com.br/'
    driver.get(url)
    time.sleep(30)  # Aguarda a página carregar

    # Encontra o script com o JSON dos produtos
    scripts = driver.find_elements(By.XPATH, '//script[@type="application/ld+json"]')
    for script in scripts:
        try:
            data = json.loads(script.get_attribute('innerHTML'))
            if data.get('@type') == 'SearchResultsPage':
                items = data['mainEntity']['itemListElement']
                for item in items:
                    produto = item['item']
                    nome = produto['name']
                    preco = produto['offers']['lowPrice']
                    link = produto['url']
                    print(f'Produto: {nome}\nPreço: R${preco}\nLink: {link}\n')
                break
        except Exception as e:
            continue

    selenium.quit_driver()

if __name__ == '__main__':
    main()
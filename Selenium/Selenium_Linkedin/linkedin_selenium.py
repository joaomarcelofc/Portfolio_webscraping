#import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parsel import Selector
from time import sleep
import csv

#Arquivo csv
writer = csv.writer(open('output_2.csv','w',encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

#Chrome driver
driver = webdriver.Chrome('./chromedriver')

#Acessar linkedin
driver.get('https://www.linkedin.com')
sleep(1)

#preencher usuário
usuario_input = driver.find_element(By.NAME,'session_key')
usuario_input.send_keys('jmfonsecacunha@gmail.com')
sleep(1)

#preencher senha
senha_input = driver.find_element(By.NAME,'session_password')
senha_input.send_keys('shortround')
sleep(1)

#clicar para logar
driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button').click()
sleep(3)

#Google
driver.get('https://www.google.com')
sleep(1)

#Selecionar o campo de busca
busca_input = driver.find_element(By.NAME,'q')

#Fazer a busca no google
busca_input.send_keys('site:linkedin.com/in AND “ciencias contabeis” AND “Arcos" AND "Minas Gerais"')
busca_input.send_keys(Keys.RETURN)
sleep(2)

#Extrair lista de perfis
lista_perfil = driver.find_elements(By.XPATH,'//*[@id="rso"]/div/div/div/div[1]/div/a')
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

#Extrair informações individuais
for perfil in lista_perfil:
    driver.get(perfil)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//title/text()').extract_first().split(' | ')[0]
    headline = response.xpath('//*[@id="ember29"]/div[2]/div[2]/div[1]/div[2]/text()').extract_first().strip()
    url_perfil = driver.current_url

    #escrever no arquivo csv
    writer.writerow([nome, headline, url_perfil])

#Sair do driver
driver.quit()


import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.topuniversities.com/university-rankings/world-university-rankings/2022')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#print(site.prettify())
universidade = site.find('a', attr={'class': 'uni-link'})
print(universidade)
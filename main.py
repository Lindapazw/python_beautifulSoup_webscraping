from bs4 import BeautifulSoup
import requests

# website
website = 'https://subslikescript.com/movie/Titanic-120338'
# pongo en la variable result el resultado
result = requests.get(website)
# creo la variable content y coloco el result y obtengo el texto
content = result.text
# creamos la variable soup para localizar elementos dentro de la web
soup = BeautifulSoup(content, 'lxml')
# imprimimos el html
print(soup.prettify())


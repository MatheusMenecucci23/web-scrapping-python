import requests
from bs4 import BeautifulSoup

#fazendo uma requisição do site
response = requests.get('https://noticias.uol.com.br/')


#pegando o conteudo inteiro
content = response.content

#criando um objeto BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

# HTML da notícia encontra a primeira div que tem essa class
noticia = site.find('div', attrs={'class': 'thumb-caption'})

# pegando somente o Título
titulo = noticia.find('h3', attrs={'class': 'thumb-title title-xsmall title-lg-small'})

print(titulo.text)


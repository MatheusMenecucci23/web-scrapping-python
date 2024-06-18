import requests
from bs4 import BeautifulSoup

#fazendo uma requisição do site
response = requests.get('https://g1.globo.com/')


#pegando o conteudo inteiro
content = response.content

#criando um objeto BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

# HTML da notícia encontra a primeira div que tem essa class
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# pegando somente o Título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print(titulo.text)

# Subtítulo: div class="feed-post-body-resumo"
subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

print(subtitulo)
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

article_titles = []

for i in soup.find_all('h3', {'class': 'indicate-hover'}):
    article_titles.append(i.text)

for x in article_titles:
    print(x)

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

article = []

for i in soup.find_all('p'):
    article.append(i.text)

for x in article:
    print(x)

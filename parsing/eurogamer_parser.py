import requests
from bs4 import BeautifulSoup




def get_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        images = []
        soup = BeautifulSoup(response.text, 'lxml')
        article_section = soup.find('div', class_='article_body')
        paragraphs = article_section.find_all('p')
        paragraphs = [p.text for p in paragraphs]
        article = ' '.join(paragraphs)
        images = article_section.find_all('img')
        images = [image['src'].split('?')[0] for image in images]
        return article, images
    else:
        print(f'Requests error:{response.status_code}')
        return None

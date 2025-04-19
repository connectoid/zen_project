import requests
from bs4 import BeautifulSoup




def get_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        images = []
        soup = BeautifulSoup(response.text, 'lxml')
        article_section = soup.find('section', class_='article-body')
        paragraphs = article_section.find_all('p')
        paragraphs = [p.text for p in paragraphs]
        article = ' '.join(paragraphs)
        try:
            images_div = article_section.find('div', class_='image-gallery__list')
            images = images_div.find_all('a')
            images = [image['href'] for image in images]
        except Exception as e:
            print(f'Images galery not found: {e}')
        try:
            images = article_section.find_all('img')
            images = [image['src'] for image in images]
        except Exception as e:
            print(f'Images not found: {e}')

        return article, images
    else:
        print(f'Requests error:{response.status_code}')
        return None

import html

import requests
from bs4 import BeautifulSoup

def get_images(source):
    images = source.find_all('img')
    images = [image['src'] for image in images]
    return images

def get_galery_html_from_script(soup):
    scripts = soup.find_all('script', {'type': 'module'})
    image_list = []
    for script in scripts:
        try:
            script_string = str(script)
            if 'window.arrayOfGalleries' in script_string:
                parts = script_string.split('=', 2)
                if len(parts) > 1:
                    html_string = parts[-1].split('</script>')[0][:-1]
                    html_string  = html.unescape(html_string)
                    html_string = html_string.replace('\\n', '\n')
                    html_string = html_string.replace('\\', '')
                    soup = BeautifulSoup(html_string, 'html.parser')
                    images = soup.find_all('img')
                    images = [image['src'] for image in images]
                    for image in images:
                        if image not in image_list:
                            image_list.append(image)
        except Exception as e:
            print(f'Galery HTML not found: {e}')
    return image_list


def get_article(url: str) -> tuple[str, list]:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        images = get_galery_html_from_script(soup)
        article_section = soup.find('section', {'id': 'article-body'})
        images = get_images(article_section)
        paragraphs = article_section.find_all(['p', 'h2', 'h3'])
        paragraphs = [p.text for p in paragraphs if p.text != ' ']
        article = ' '.join(paragraphs)
        return article, images
    else:
        print(f'Request Error: {response.status_code}')

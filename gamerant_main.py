from gpt.deepseek import get_translation
from parsing.gamerant_parser import get_article
from tools.tools import download_images, remove_images, clear_text, save_text_to_file, create_game_folder

url = 'https://gamerant.com/best-ps5-games-playstation-plus-premium-extra/'
url = 'https://gamerant.com/last-of-us-part-2-remastered-pc-review/'
url = 'https://gamerant.com/first-berserker-khazan-review/'
url = 'https://gamerant.com/assassins-creed-shadows-review/'
url = 'https://gamerant.com/kingdom-come-deliverance-2-review/'
url = 'https://gamerant.com/the-sims-4-review/'
url = 'https://gamerant.com/atomfall-review/'
url = 'https://gamerant.com/path-of-exile-2-early-access-review/'
url = 'https://gamerant.com/fallout-elder-scrolls-hidden-connections/'
url = 'https://gamerant.com/sid-meiers-civilization-7-review/'
url = 'https://gamerant.com/kaiserpunk-review/'
url = 'https://gamerant.com/inzoi-early-access-review/'
url = 'https://gamerant.com/post-apocalyptic-games-like-atomfall-fallout/'
url = 'https://gamerant.com/blue-prince-review/'


outro_text = 'Понравилась статья? Лайк + Подписка = Комбо-удар в поддержку нашего канала! Не пропустите новые обзоры, игровые новости и интересные подборки! '

game_path = url.split('/')[3]
target_path = f'/Users/alexanderbeley/Documents/Dzen/Gamerant/{game_path}/'
create_game_folder(target_path)
article, images = get_article(url)
print(f'Найдено {len(images)} изображений')
remove_images(target_path)
download_images(images, target_path)
translatated_article = get_translation(article)
cleared_translatated_article = clear_text(translatated_article)
cleared_translatated_article = cleared_translatated_article + '\n' + outro_text
save_text_to_file(cleared_translatated_article, target_path)
print(cleared_translatated_article)
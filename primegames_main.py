from gpt.deepseek import get_translation
from parsing.primegames_parser import get_article
from tools.tools import download_images, remove_images, clear_text, save_text_to_file, create_game_folder

url = 'https://primagames.com/reviews/tempest-rising-review'

outro_text = 'Понравилась статья? Лайк + Подписка = Комбо-удар в поддержку нашего канала! Не пропустите новые обзоры, игровые новости и интересные подборки! '

game_path = url.split('/')[4]
target_path = f'/Users/alexanderbeley/Documents/Dzen/Primegames/{game_path}/'
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
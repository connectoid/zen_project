import os
import shutil

import requests


def clear_text(text):
    text = text.replace('*', '').replace('#', '').replace('---', '')
    return text


def create_game_folder(target_path):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
        os.makedirs(target_path)
    else:
        os.makedirs(target_path)


def remove_images(target_path, output_folder='images'):
    output_folder = target_path + output_folder
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
        os.makedirs(output_folder)
    else:
        os.makedirs(output_folder)


def download_images(image_urls, target_path, output_folder='images'):
    output_folder = target_path + output_folder
    for url in image_urls:
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                filename = os.path.join(output_folder, url.split('/')[-1])
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f'Файл {filename} успешно загружен.')
            else:
                print(f'Ошибка при загрузке файла {url}. Код статуса: {response.status_code}')
        except Exception as e:
            print(f'Не удалось скачать файл {url}: {e}')


def save_text_to_file(string, target_path, filename='article.txt'):
    filename = target_path + filename
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(string)
        print(f'Текст успешно сохранен в файл {filename}')
    except Exception as e:
        print(f'Ошибка при сохранении текста в файл: {e}')


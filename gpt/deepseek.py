import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEP_SEEK_API_KEY')
BASE_DEEPSEEK_URL = 'https://api.deepseek.com'
DEEPSEEK_API_KEY = 'sk-7df9a4c320d849a7b25a1d40b69516fe'


translation_prompt_intro = """
        Переведи следующий текст на русский язык как профессиональный переводчик, 
        разбирающийся в видеоиграх. Текст должен быть стилистически грамотно написан, 
        не должен быть похож на машинный перевод. Добавляй в текст комментарии от первого лица, 
        как будто ты человек играющий в игры. Текст должен выглядеть как будто его написал 
        профессиональный автор статей про компьютерные игры. Придай тексту живой характер. 
        Не пиши ничего от себя, дай только переведенный текст. Убери все лишние символы вроде * и ":
    """


def get_translation(prompt):
    prompt = f'{translation_prompt_intro} {prompt}'
    print(f'Fetch data ...')
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=BASE_DEEPSEEK_URL)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    response_json = response.json()
    print(f'Recived response: {response_json}')
    answer = response.choices[0].message.content
    print(answer)
    return answer
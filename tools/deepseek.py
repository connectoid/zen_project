import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEP_SEEK_API_KEY')
BASE_DEEPSEEK_URL = 'https://api.deepseek.com'
DEEPSEEK_API_KEY = 'sk-7df9a4c320d849a7b25a1d40b69516fe'
print(DEEPSEEK_API_KEY)


def get_answer(prompt):
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
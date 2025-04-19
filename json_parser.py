from pprint import pprint

import requests

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'origin': 'https://gamerant.com',
    'priority': 'u=1, i',
    'referer': 'https://gamerant.com/first-berserker-khazan-review/',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

params = {
    'v': '26',
}

response = requests.get(
    'https://cdn.adsninja.ca/api/cached/valnetinc/GameRant/adsInjectorConfigs.json',
    params=params,
    headers=headers,
)

pprint(response.json())
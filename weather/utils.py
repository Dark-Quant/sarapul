import json

import requests
from django.core.cache import cache


def get_forecast():
    if not cache.get('weather'):
        params = {
            'lat': 56.47633,
            'lon': 53.79782,
            'lang': 'ru_RU',
            'limit': 7,
            'hours': False,
            'extra': True
        }
        w = requests.get("https://api.weather.yandex.ru/v2/forecast", params=params,
                         headers={'X-Yandex-API-Key': '7734821e-b97e-4f28-80a5-8b74bd73fe1b'})
        cache.set('weather', json.loads(w.text), 60 * 60 * 6)
    return cache.get('weather')

from django import template

from weather.utils import *

register = template.Library()
translating = {
    'condition': {
        'clear': 'Ясно',
        'partly-cloudy': 'Малооблачно',
        'cloudy': 'Облачно с прояснениями',
        'overcast': 'Пасмурно',
        'drizzle': 'Морось',
        'light-rain': 'Небольшой дождь',
        'rain': 'Дождь',
        'moderate-rain': 'Умеренно сильный дождь',
        'heavy-rain': 'Сильный дождь.',
        'continuous-heavy-rain': 'Длительный сильный дождь',
        'showers': 'Ливень',
        'wet-snow': 'Дождь со снегом',
        'light-snow': 'Небольшой снег',
        'snow': 'Снег',
        'snow-showers': 'Снегопад',
        'hail': 'Град',
        'thunderstorm': 'Гроза',
        'thunderstorm-with-rain': 'Дождь с грозой',
        'thunderstorm-with-hail': 'Гроза с градом',
    },
    'wind_dir': {
        'nw': 'СВ',
        'w': 'В',
        'sw': 'ЮВ',
        's': 'Ю',
        'se': 'ЮЗ',
        'e': 'З',
        'ne': 'СЗ',
        'n': 'С',
    }
}


@register.inclusion_tag('weather/block_of_weather.html')
def block_of_weather():
    return {'fact': get_forecast()['fact']}


@register.simple_tag()
def translate_weather_fields(key, value):
    return translating[key][value]

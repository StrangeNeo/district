import sys
from PIL import Image
import requests
from io import BytesIO

here = ' '.join(sys.argv[1:])


def apt(addr):
    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    geo_params = {
        "apikey": api_key,
        "geocode": addr,
        "format": "json",
        'kind': 'district'
    }
    response = requests.get(geocoder_api_server, params=geo_params).json()
    pos = ','.join(response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split())

    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    geo_params = {
        "apikey": api_key,
        "geocode": pos,
        "format": "json",
        'kind': 'district'
    }
    response = requests.get(geocoder_api_server, params=geo_params)

    response = response.json()
    print(response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components'][5]['name'])


apt(here)

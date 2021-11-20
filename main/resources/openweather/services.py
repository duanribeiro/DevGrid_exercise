import requests
from flask import current_app
from flask_restplus import Api, fields, Resource, marshal
from main.resources.openweather.serializers import response_model
import json


class Temperature:

    @staticmethod
    def get_by_city_name(city_name):
        OPENWEATHER_ENDPOINT = current_app.config['OPENWEATHER_ENDPOINT']
        OPENWEATHER_APIKEY = current_app.config['OPENWEATHER_APIKEY']

        response = requests.get(f'{OPENWEATHER_ENDPOINT}?q={city_name}&appid={OPENWEATHER_APIKEY}')
        content = json.loads(response.content)

        avg = (float(content['main']['temp_min']) + float(content['main']['temp_max'])) / 2
        response_temperature_model = {
            'min': content['main']['temp_min'],
            'max': content['main']['temp_max'],
            'avg': round(avg, 2),
            'feels_like': content['main']['feels_like'],
            'city': {
                'name': content['name'],
                'country': content['sys']['country']
            }
        }

        return response_temperature_model

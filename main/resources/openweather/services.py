import requests
from flask import current_app, abort
import json
from main.helpers.redis import set_to_cache, check_max_keys, client, get_from_cache


class Temperature:

    @staticmethod
    def get_by_city_name(city_name):
        endpoint = current_app.config['OPENWEATHER_ENDPOINT']
        apikey = current_app.config['OPENWEATHER_APIKEY']
        default_max_number = current_app.config['DEFAULT_MAX_NUMBER']

        response = requests.get(f'{endpoint}?q={city_name}&appid={apikey}')
        if response.status_code == 404:
            abort(404)

        content = json.loads(response.content)
        avg = (float(content['main']['temp_min']) + float(content['main']['temp_max'])) / 2

        result = {
            'min': content['main']['temp_min'],
            'max': content['main']['temp_max'],
            'avg': round(avg, 2),
            'feels_like': content['main']['feels_like'],
            'city': {
                'name': content['name'],
                'country': content['sys']['country']
            }
        }

        if check_max_keys() < default_max_number:
            set_to_cache(key=city_name, value=result)

        return result

    @staticmethod
    def get_by_length(length):
        result = []
        for key in list(client.scan_iter("*"))[:length]:
            result.append(get_from_cache(key))

        return result

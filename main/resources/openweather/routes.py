from flask_restplus import Resource, Namespace
from main.resources.openweather.services import Temperature
from main.resources.openweather.serializers import response_model
from main.helpers.redis import get_from_cache
from flask import request, current_app, abort
import logging

logger = logging.getLogger(__name__)
ns = Namespace('', description='Open Weather Wrapper')


def check_cache(func):
    def wrapper(*args, **kwargs):
        """Wrapper decorator to be used on check is the data is cached

        :param kwargs: City name to be searched on cache
        :return JSON data about city
        """
        cache = get_from_cache(kwargs['city_name'])
        if cache:
            return cache
        return func(*args, **kwargs)

    return wrapper


@ns.route('/temperature/<string:city_name>')
class TemperatureByCityName(Resource):
    @ns.doc(responses={
        200: 'Success',
        400: 'Bad Request',
        404: 'Not found',
        500: 'Internal Server Error'
    }, security=None)
    @ns.doc(params={'city_name': "Get the current temperature for the specified {city_name}"})
    @ns.marshal_with(response_model)
    @check_cache
    def get(self, city_name):
        """Get the current temperature for the specified city_name, either from cache or from the Open Weather API"""
        return Temperature.get_by_city_name(city_name)


@ns.route('/temperature')
class TemperatureMain(Resource):
    @ns.doc(responses={
        200: 'Success',
        400: 'Bad Request',
        404: 'Not found',
        500: 'Internal Server Error'
    }, security=None)
    @ns.marshal_list_with(response_model)
    @ns.doc(params={
        'max': {
            'type': 'int',
            'description': 'Get the cached temperatures for up to the latest max_number queried cities that are still '
                           'valid.'
        }
    })
    def get(self):
        """Get the cached temperatures for up to the latest max_number queried cities that are still valid"""
        length = int(request.args.get('max')) if request.args.get('max') else current_app.config['DEFAULT_MAX_NUMBER']

        return Temperature.get_by_length(length)

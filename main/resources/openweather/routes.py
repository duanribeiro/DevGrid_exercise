from flask_restplus import Resource, Namespace
from main.resources.openweather.services import Temperature
from main.resources.openweather.serializers import response_model
from main.helpers.redis import get_from_cache

import logging


logger = logging.getLogger(__name__)
ns = Namespace('', description='Open Weather Wrapper')


def check_cache(func):
    def wrapper(*args, **kwargs):
        cache = get_from_cache(kwargs['city_name'])
        if cache:
            return cache
        return func(*args, **kwargs)
    return wrapper


@ns.route('/temperature/<string:city_name>')
class TemperatureByCityName(Resource):
    @ns.doc(responses={
        200: 'Success',
        404: 'Not found.',
        500: 'Internal Server Error'
    }, security=None)
    @ns.doc(params={'city_name': "Get the current temperature for the specified {city_name}"})
    @ns.marshal_with(response_model)
    @check_cache
    def get(self, city_name):
        """
        Temperature endpoint
        """
        return Temperature.get_by_city_name(city_name)




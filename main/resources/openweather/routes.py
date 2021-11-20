from flask_restplus import Resource, Namespace
from flask import Flask, request, jsonify
import logging

logger = logging.getLogger(__name__)
api = Namespace('', description='Open Weather Wrapper')


@api.route('/temperature/<string:city_name>')
class Temperature(Resource):

    @api.doc(responses={
        200: 'Success',
        404: 'Not found.',
        500: 'Internal Server Error'
    }, security=None)
    @api.doc(params={'city_name': "Get the current temperature for the specified {city_name}"})
    def get(self):
        """
        Temperature endpoint
        """
        return 1




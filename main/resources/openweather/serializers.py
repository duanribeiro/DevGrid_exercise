from main import api
from flask_restplus import fields

city_model = api.model('City Model', {
    'country ': fields.String(required=True, description=""),
    'name': fields.String(required=True, description="Queried city's name."),
})

response_model = api.model('Temperature Response Model', {
    'min': fields.Float(required=True, description='Minimum temperature in degrees Celsius.'),
    'max': fields.Float(required=True, description='Maximum temperature in degrees Celsius.'),
    'avg': fields.Float(required=True, description='Average temperature in degrees Celsius.'),
    'feels_like': fields.Float(required=True, description='Feels like temperature in degrees Celsius.'),
    'city': fields.Raw(city_model)
})

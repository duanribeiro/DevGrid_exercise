from main import api
from flask_restplus import fields

"""Flask-RESTPlus provides an easy way to control what data you actually render in your response or expect as in 
input payload. With the fields module, you can use whatever objects (ORM models/custom classes/etc.) you want in your 
resource also lets you format and filter the response so you don’t have to worry about exposing internal data 
structures. 

It’s also very clear when looking at your code what data will be rendered and how it will be formatted.
"""

city_model = api.model('City Model', {
    'country ': fields.String(required=True, description="Queried city's country code in the ISO 3166-1 format."),
    'name': fields.String(required=True, description="Queried city's name."),
})

response_model = api.model('Temperature Response Model', {
    'min': fields.Float(required=True, description='Minimum temperature in degrees Celsius.'),
    'max': fields.Float(required=True, description='Maximum temperature in degrees Celsius.'),
    'avg': fields.Float(required=True, description='Average temperature in degrees Celsius.'),
    'feels_like': fields.Float(required=True, description='Feels like temperature in degrees Celsius.'),
    'city': fields.Raw(city_model)
})

from flask import Blueprint
from flask_restplus import Api
import logging

logger = logging.getLogger(__name__)
v1_blueprint = Blueprint('v1', __name__, url_prefix='')

api = Api(v1_blueprint,
          doc='/swagger',
          title='API Documentation',
          version='0.0.1',
          description="""Design and build a wrapper for the Open Weather API current weather data service that returns
                         a city's temperature, with caching, also allowing for the temperature of the latest queried cities
                         that are still validly cached to be retrieved.""",)

from main.resources.openweather.routes import ns as openweather_namespace
api.add_namespace(openweather_namespace)

from flask import Blueprint, request
from flask_restplus import Api
import logging

logger = logging.getLogger(__name__)
v1_blueprint = Blueprint('v1', __name__, url_prefix='')

api = Api(v1_blueprint,
          doc='/swagger',
          title='API Documentation',
          version='1.0',
          description='Flask RESTful API')


from main.resources.openweather.routes import api as openweather_namespace
api.add_namespace(openweather_namespace)


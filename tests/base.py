from flask_testing import TestCase
from app import app
import config


class BaseTestCase(TestCase):
    """ Default base test case using the Dev configs """

    def create_app(self):
        app.config.from_object(config.DevConfig)
        return app

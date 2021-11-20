import os
import unittest
from flask_testing import TestCase
from app import app
import config


class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object(config.DevConfig)
        return app

    def test_app_is_development(self):
        """ Test enviroment variables """
        self.assertTrue(app.config['DEBUG'] is True)


class TestProdConfig(TestCase):
    def create_app(self):
        app.config.from_object(config.ProdConfig)
        return app

    def test_app_is_production(self):
        """ Test enviroment variables """
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()

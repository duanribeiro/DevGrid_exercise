import unittest
import json
from tests.base import BaseTestCase
import time


class TestRequestByCityName(BaseTestCase):
    def test_found(self):
        """ Test data when city is found """
        with self.client:
            city_name = "Lima"
            response = self.client.get(f'/temperature/{city_name}')
            self.assertEqual(response.status_code, 200)

            data = json.loads(response.data.decode())
            self.assertEqual(city_name, data['city']['name'])
            self.assertIsInstance(data['min'], float)
            self.assertIsInstance(data['max'], float)
            self.assertIsInstance(data['avg'], float)
            self.assertIsInstance(data['feels_like'], float)

    def test_not_found(self):
        """ Test data when city is not found """
        with self.client:
            city_name = "!@#!@$!%!#%!#"
            response = self.client.get(f'/temperature/{city_name}')
            self.assertEqual(response.status_code, 404)

    def test_cache(self):
        """ Test cached data on redis """
        with self.client:
            city_name = "New York"

            response = self.client.get(f'/temperature/{city_name}')
            data = json.loads(response.data.decode())
            time.sleep(1)

            new_response = self.client.get(f'/temperature/{city_name}')
            new_data = json.loads(new_response.data.decode())
            self.assertEqual(data, new_data)


if __name__ == '__main__':
    unittest.main()

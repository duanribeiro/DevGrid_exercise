import unittest
import json
from tests.base import BaseTestCase
from main.helpers.redis import client


class TestRequestTemperature(BaseTestCase):
    def test_records_cached(self):
        """ Test records cached on redis """
        client.flushall()
        with self.client:
            cities = ["Tokyo", "Dublin", "Paris"]
            for city_name in cities:
                self.client.get(f'/temperature/{city_name}')

            response = self.client.get(f'/temperature')
            data = json.loads(response.data.decode())

            self.assertEqual("Tokyo", data[0]['city']['name'])
            self.assertEqual("Dublin", data[1]['city']['name'])
            self.assertEqual("Paris", data[2]['city']['name'])
            self.assertEqual(len(data), 3)


if __name__ == '__main__':
    unittest.main()

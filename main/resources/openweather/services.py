import json
from bson.json_util import dumps
from datetime import datetime


class CacheManager:

    @staticmethod
    def save_cache(payload):
        return 1
        # return json.loads(dumps(responses))

    @staticmethod
    def load_cache(payload):
        return 1
        # return json.loads(dumps(responses))

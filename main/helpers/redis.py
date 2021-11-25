from datetime import timedelta
from flask import current_app
import redis
import json
from config import REDIS_ENDPOINT, REDIS_PORT

client = redis.Redis(
    host=REDIS_ENDPOINT,
    port=REDIS_PORT,
    db=0,
    socket_timeout=5,
)


def get_from_cache(key):
    """Get data from redis.
    
    :param key: Key name to be searched on redis
    :return Parsed JSON data from redis if exists
    """
    data = client.get(key)
    return json.loads(data) if data else None


def set_to_cache(key, value):
    """Save data on redis.
    
    :param key: name to be searched on redis
    :param value: Data to be saved on redis
    :return True if save with success
    """
    cache_ttl = current_app.config['CACHE_TTL_SECONDS']
    state = client.set(key, value=json.dumps(value), ex=timedelta(seconds=cache_ttl))
    return state


def check_max_keys():
    """Save data on redis.
    
    :return Integer with number os keys cached on redis
    """
    return len(list(client.scan_iter("*")))

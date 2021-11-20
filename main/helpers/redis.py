from datetime import timedelta
from flask import current_app
import redis
import json

client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    socket_timeout=5,
)


def get_from_cache(key):
    """Get data from redis."""
    data = client.get(key)
    return json.loads(data) if data else None


def set_to_cache(key, value):
    """Set data to redis."""
    cache_ttl = current_app.config['CACHE_TTL_SECONDS']
    state = client.set(key, value=json.dumps(value), ex=timedelta(seconds=cache_ttl))
    return state


def check_max_keys():
    """Check how many keys exists on redis"""
    return len(list(client.scan_iter("*")))


import logging
import sys
import os

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger('__name__')
REDIS_ENDPOINT = os.environ['REDIS_ENDPOINT']
REDIS_PORT = os.environ['REDIS_PORT']


class BaseConfig:
    DEBUG = True
    RESTPLUS_VALIDATE = True
    ERROR_INCLUDE_MESSAGE = False
    RESTPLUS_MASK_SWAGGER = False
    PROPAGATE_EXCEPTIONS = True

    try:
        OPENWEATHER_ENDPOINT = os.environ['OPENWEATHER_ENDPOINT']
        OPENWEATHER_APIKEY = os.environ['OPENWEATHER_APIKEY']
        CACHE_TTL_SECONDS = int(os.environ['CACHE_TTL_SECONDS'])
        DEFAULT_MAX_NUMBER = int(os.environ['DEFAULT_MAX_NUMBER'])
        logger.info('Enviroment variables loaded.')

    except KeyError as key:
        logger.critical(f'{key} env var is missing !')
        sys.exit()


class ProdConfig(BaseConfig):
    DEBUG = False


class DevConfig(BaseConfig):
    pass





import logging
import sys


class BaseConfig:
    # Logger configs
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger('__name__')

    # Other configs
    DEBUG = True
    RESTPLUS_VALIDATE = True
    ERROR_INCLUDE_MESSAGE = False
    # RESTPLUS_MASK_SWAGGER = False
    PROPAGATE_EXCEPTIONS = True

    # Env variables
    try:
        OPENWEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
        OPENWEATHER_APIKEY = '5ba6e1ac0975af545801d9227ad1e376'
        logger.info('Enviroment variables loaded.')

    except KeyError as key:
        logger.critical(f'{key} env var is missing !')
        sys.exit()


class ProdConfig(BaseConfig):
    DEBUG = False


class DevConfig(BaseConfig):
    pass





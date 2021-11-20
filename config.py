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
    RESTPLUS_MASK_SWAGGER = False
    PROPAGATE_EXCEPTIONS = True

    try:
        JWT_SECRET_KEY = "L9ThxnotKPzthJ7hu3bnORuT6xI="
        logger.info('Enviroment variables loaded.')

    except KeyError as key:
        logger.critical(f'{key} env var is missing !')
        sys.exit()


class ProdConfig(BaseConfig):
    DEBUG = False


class DevConfig(BaseConfig):
    pass





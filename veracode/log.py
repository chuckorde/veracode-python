import logging
import os

def veracode_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s, %(levelname)s, %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get('VERACODE_LOG_LEVEL', logging.NOTSET))
    logger.addHandler(handler)
    return logger


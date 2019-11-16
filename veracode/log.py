import logging, os

def veracode_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s, %(levelname)s, %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    loglevel = os.environ.get('VERACODE_LOG_LEVEL', None)

    if loglevel:
        logger.setLevel(getattr(logging, loglevel))
    else:
        # logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.NOTSET)

    logger.addHandler(handler)
    return logger

import logging, os

def veracode_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s, %(levelname)s, %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
<<<<<<< HEAD
    logger.setLevel(os.environ.get('VERACODE_LOG_LEVEL', logging.NOTSET))
=======
    loglevel = os.environ.get('VERACODE_LOG_LEVEL', None)

    if loglevel:
        logger.setLevel(getattr(logging, loglevel))
    else:
        # logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.NOTSET)

>>>>>>> c0a9f98d75532b7195b043cc3780384b00b806f8
    logger.addHandler(handler)
    return logger


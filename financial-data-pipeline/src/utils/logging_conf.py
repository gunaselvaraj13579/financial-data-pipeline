import logging, sys

def get_logger(name):
    logger=logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        h=logging.StreamHandler(sys.stdout)
        h.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s','%Y-%m-%d %H:%M:%S'))
        logger.addHandler(h)
    return logger

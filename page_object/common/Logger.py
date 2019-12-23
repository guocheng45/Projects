import logging


class Logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    _ch = logging.StreamHandler()
    _fmt = logging.Formatter('[%(asctime)s %(filename)s Line: %(lineno)d][%(levelname)s]: %(message)s')
    _ch.setFormatter(_fmt)
    logger.addHandler(_ch)


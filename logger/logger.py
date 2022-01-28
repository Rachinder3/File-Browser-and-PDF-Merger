import logging


class Logger():
    def __init__(self, filename):
        logging.basicConfig(filename=filename, format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

    def add_log(self, message, mode='info'):
        if mode == 'debug':
            logging.debug(message)

        if mode == 'info':
            logging.info(message)

        if mode == 'warning':
            logging.warning(message)

        if mode == 'error':
            logging.error(message)

        if mode == 'critical':
            logging.critical(message)
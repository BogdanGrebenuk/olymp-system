import logging.config


def init_logging(logger_config):
    logging.config.dictConfig(logger_config)

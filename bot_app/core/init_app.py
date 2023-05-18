import logging


from ..settings.log import DEFAULT_LOGGING


def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)
    
    
    
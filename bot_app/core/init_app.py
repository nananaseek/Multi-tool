import logging


from ..settings.log import DEFAULT_LOGGING


def configure_logging(log_settings: dict = None):
    """
    Налаштовує логування за допомогою переданого словника налаштувань.

    Args:
        log_settings (dict, optional): Словник налаштувань логування. За замовчуванням використовується `DEFAULT_LOGGING`.

    Returns:
        None

    """
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)

    
    
    
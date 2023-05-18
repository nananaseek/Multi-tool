import logging

from .handlers import *
from .utils import *
from .conf import DEFAULT_LOGGING


log_settings = DEFAULT_LOGGING
logging.config.dictConfig(log_settings)


logging.warning('Start bot')
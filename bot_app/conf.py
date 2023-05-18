from dotenv import load_dotenv

import os
import logging.config


# Визначте шлях до файлу .env в папці config
env_path = os.path.join("config", ".env")

# Завантажте змінні середовища з файлу .env
load_dotenv(dotenv_path=env_path)

# Передавання токену в бота
TOKEN = os.getenv('TOKEN')
# Перемикач режима відладки
DEBUG = os.getenv('DEBUG')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
LOGS_ROOT = os.path.join(PROJECT_ROOT, "bot_app/logs")
TEMP_FOLDER = f"{PROJECT_ROOT}/temp/" 

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'app.settings.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'app.settings.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'main_formatter': {
            'format': '[%(levelname)s]:[%(name)s]: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{LOGS_ROOT}/bot_main.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'main_formatter',
            'filters': ['require_debug_false'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{LOGS_ROOT}/bot_main_debug.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },

    }
}


class RequireDebugFalse(logging.Filter):
    def filter(self, record):
        return not DEBUG


class RequireDebugTrue(logging.Filter):
    def filter(self, record):
        return DEBUG

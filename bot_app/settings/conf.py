from dotenv import load_dotenv

import os


class Settings:
    # Визначте шлях до файлу .env в папці config
    ENV_PATH = os.path.join("config", ".env")

    # Завантажте змінні середовища з файлу .env
    load_dotenv(dotenv_path=ENV_PATH)

    # Передавання токену в бота
    TOKEN = os.getenv('TOKEN')
    # Перемикач режима відладки
    DEBUG = bool(os.getenv('DEBUG'))

    ENDPOINT = 'http://127.0.0.1:8000/'
    CONVERTOR_ENDPOINT = ENDPOINT + 'convertor/'
    AUDIO_ENDPOINT = CONVERTOR_ENDPOINT + 'audio'
    VIDEO_ENDPOINT = CONVERTOR_ENDPOINT + 'video'
    PHOTO_ENDPOINT = CONVERTOR_ENDPOINT + 'picture'


    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    LOGS_ROOT = os.path.join(PROJECT_ROOT, "logs")
    TEMP_FOLDER = f"{PROJECT_ROOT}/temp/" 


settings = Settings()

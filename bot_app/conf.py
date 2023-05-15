from dotenv import load_dotenv
import os

# Визначте шлях до файлу .env в папці config
env_path = os.path.join("config", ".env")

# Завантажте змінні середовища з файлу .env
load_dotenv(dotenv_path=env_path)

# Передавання токену в бота
TOKEN = os.getenv('TOKEN')
# Перемикач режима відладки
DEBUG = os.getenv('DEBUG')
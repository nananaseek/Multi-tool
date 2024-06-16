from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Підключення налаштувань бота 
from .settings.conf import settings
from .core.init_app import configure_logging


bot = Bot(token=settings.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

configure_logging()
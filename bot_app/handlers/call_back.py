from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_app.app import dp
from ..states import AudioHandler, VideoHandler, PhotoHandler
from ..core.message import FORMAT_HANDLER, PHOTO_WARNING

    
"""
Функції для входу в сценарій
"""
    
# Функція для визову сценарію file_handler при натисканні inline кнопки "Аудіо"
@dp.callback_query_handler(lambda query: query.data == 'audio')
async def audio_callback(query: types.CallbackQuery, state: FSMContext):
    await AudioHandler.file_handler.set()
    await query.message.answer(FORMAT_HANDLER)

# Функція для визову сценарію file_handler при натисканні inline кнопки "Відео"
@dp.callback_query_handler(lambda query: query.data == 'video')
async def video_callback(query: types.CallbackQuery, state: FSMContext):
    await VideoHandler.file_handler.set()
    await query.message.answer(FORMAT_HANDLER)

# Функція для визову сценарію file_handler при натисканні inline кнопки "Фото"
@dp.callback_query_handler(lambda query: query.data == 'photo')
async def photo_callback(query: types.CallbackQuery, state: FSMContext):
    await PhotoHandler.file_handler.set()
    await query.message.answer(PHOTO_WARNING)
    await query.message.answer(FORMAT_HANDLER)
    


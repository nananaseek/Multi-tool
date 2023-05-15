from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import dp
from ..states import FileHandlerGroup
from ..message import FORMAT_HANDLER

    
"""
Функції для входу в сценарій
"""
    
# Функція для визову сценарію file_handler при натисканні inline кнопки "Аудіо"
@dp.callback_query_handler(lambda query: query.data == 'audio', state='*')
async def audio_callback(query: types.CallbackQuery, state: FSMContext):
    await FileHandlerGroup.file_handler.set()
    await query.message.answer(FORMAT_HANDLER)

# Функція для визову сценарію file_handler при натисканні inline кнопки "Відео"
@dp.callback_query_handler(lambda query: query.data == 'video', state='*')
async def video_callback(query: types.CallbackQuery, state: FSMContext):
    await FileHandlerGroup.file_handler.set()
    await query.message.answer(FORMAT_HANDLER)

# Функція для визову сценарію file_handler при натисканні inline кнопки "Фото"
@dp.callback_query_handler(lambda query: query.data == 'photo', state='*')
async def photo_callback(query: types.CallbackQuery, state: FSMContext):
    await FileHandlerGroup.file_handler.set()
    await query.message.answer(FORMAT_HANDLER)
    


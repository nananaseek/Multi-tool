import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import dp
from ..states import FileHandlerGroup
from ..core.utils.file import save_file_to_memory
# from ..API.convertor.audio import 


@dp.message_handler(content_types=types.ContentType.VOICE, state=FileHandlerGroup.file_handler)
@dp.message_handler(content_types=types.ContentType.AUDIO, state=FileHandlerGroup.file_handler)
async def handle_audio_message(message: types.Message, state: FSMContext):
    try:
        # Отримуємо аудіо, на яке відповідає користувач
        audio = message.audio

        # Зберігаємо аудіо в оперативну пам'ять
        audio_bytes = await save_file_to_memory(audio)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        # async with state.proxy() as data:
        await state.update_data(audio=audio_bytes.getvalue())
            # data['audio'] = audio_bytes.getvalue()
            
        logging.info(f'File {audio} saved, entering to next stage')
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️')  
        await FileHandlerGroup.next()    
          
    except Exception as e:  
        logging.error(f'File wasn`t received, {e}')
    
    
@dp.message_handler(content_types=types.ContentType.TEXT, state=FileHandlerGroup.format_handler)
async def formatHandler(message: types.Message, state: FSMContext):
    
    format_file = message.text
    await state.update_data(format=format_file)

    await state.finish()
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import dp
from ..states import FileHandlerGroup
from ..core.utils.file import save_file_to_memory
from ..API.convertor.audio import convert_audio



@dp.message_handler(content_types=types.ContentType.VOICE, state=FileHandlerGroup.file_handler)
@dp.message_handler(content_types=types.ContentType.AUDIO, state=FileHandlerGroup.file_handler)
async def handle_audio_message(message: types.Message, state: FSMContext):
    try:
        # Отримуємо аудіо, на яке відповідає користувач
        audio = message.audio

        # Зберігаємо аудіо в оперативну пам'ять
        audio_bytes = await save_file_to_memory(audio)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        await state.update_data(audio=audio_bytes.getvalue())
        await state.update_data(origin_file_name=audio.file_name)
        await state.update_data(title=audio.title)
        await state.update_data(performer=audio.performer)
        await state.update_data(duration=audio.duration)
        await state.update_data(thumb=audio.thumb)
        
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️')  
        await FileHandlerGroup.next()    
          
    except Exception as e:  
        logging.error(f'File wasn`t received, {e}')
    
    
@dp.message_handler(content_types=types.ContentType.TEXT, state=FileHandlerGroup.format_handler)
async def formatHandler(message: types.Message, state: FSMContext):
    
    format_file = message.text
    
    async with state.proxy() as data:
        
        converted_file = await convert_audio(file=data['audio'], file_format=format_file, origin_file_name=data['origin_file_name'])
        
        file_name = data['origin_file_name']
        title = data['title']
        performer = data['performer']
        duration = data['duration']
        thumb = data['thumb']
        
        logging.debug(converted_file)
    
    is_title = title if data['title'] else file_name
    
    await message.answer_audio(converted_file, title=is_title, performer=performer,  duration=duration, thumb=thumb, caption_entities='fdsafdsa')
    
    await state.finish()
    
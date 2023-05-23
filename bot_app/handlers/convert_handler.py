import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import dp
from ..states import AudioHandler, VideoHandler, PhotoHandler
from ..core.utils.file import save_file_to_memory
from ..API.convertor import convert_audio, convert_video, convert_photo



@dp.message_handler(content_types=types.ContentType.VOICE, state=AudioHandler.file_handler)
@dp.message_handler(content_types=types.ContentType.AUDIO, state=AudioHandler.file_handler)
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
        await AudioHandler.next()    
          
    except Exception as e:  
        logging.error(f'File wasn`t received, {e}')
    
    
@dp.message_handler(content_types=types.ContentType.TEXT, state=AudioHandler.format_handler)
async def formatHandler(message: types.Message, state: FSMContext):
    
    format_file = message.text
    
    async with state.proxy() as data:
        
        file_name = data['origin_file_name']
        title = data['title']
        performer = data['performer']
        duration = data['duration']
        thumb = data['thumb']
        
        converted_file = await convert_audio(file=data['audio'], file_format=format_file, origin_file_name=file_name)
    
    is_title = title if data['title'] else file_name
    
    await message.answer_audio(converted_file, title=is_title, performer=performer,  duration=duration, thumb=thumb, allow_sending_without_reply=True)
    
    await state.finish()
    


"""
Функції для обробки відео повідоммлень
"""


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=VideoHandler.file_handler)
@dp.message_handler(content_types=types.ContentType.VIDEO, state=VideoHandler.file_handler)
async def handle_video_message(message: types.Message, state: FSMContext):
    try:
        # Отримуємо аудіо, на яке відповідає користувач
        video = message.video if message.video else message.document

        # Зберігаємо аудіо в оперативну пам'ять
        video_bytes = await save_file_to_memory(video)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        await state.update_data(video=video_bytes.getvalue())
        if message.video:
            await state.update_data(duration=video.duration)
            await state.update_data(height=video.height)
            await state.update_data(width=video.width)
        else:
            await state.update_data(is_video=message.video)
        
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️')  
        await VideoHandler.next()    
          
    except Exception as e:  
        logging.error(f'File wasn`t received, {e}')
        

@dp.message_handler(content_types=types.ContentType.TEXT, state=VideoHandler.format_handler)
async def videoformatHandler(message: types.Message, state: FSMContext): 
    
    format_file = message.text
    
    async with state.proxy() as data:
        
        is_video = data['is_video']
        
        if is_video:
            duration = data['duration']
            height = data['height']
            width = data['width']
        
        converted_file = await convert_video(file=data['video'], file_format=format_file)
            
    if is_video:
        await message.answer_video(converted_file,  duration=duration, height=height, width=width, allow_sending_without_reply=True )
    else:
        await message.answer_video(converted_file, allow_sending_without_reply=True )
        
    await state.finish()
    
    
"""
Функції для обробки фотографій
"""

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PhotoHandler.file_handler)
@dp.message_handler(content_types=types.ContentType.PHOTO, state=PhotoHandler.file_handler)
async def handle_photo_message(message: types.Message, state: FSMContext):
    try:
        
        is_photo = message.photo
        
        # Отримуємо аудіо, на яке відповідає користувач
        photo = message.photo[-1] if is_photo else message.document
        
        # Зберігаємо аудіо в оперативну пам'ять
        photo_bytes = await save_file_to_memory(photo)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        if is_photo:
            pass
        else:
            await state.update_data(photo=photo_bytes.getvalue())
            await state.update_data(origin_file_name=photo.file_name)
        
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️')  
        await PhotoHandler.next()    
          
    except Exception as e:  
        logging.error(f'File wasn`t received, {e}')
        

@dp.message_handler(content_types=types.ContentType.TEXT, state=PhotoHandler.format_handler)
async def photoformatHandler(message: types.Message, state: FSMContext): 
    
    format_file = message.text
    
    async with state.proxy() as data:
        
        file_name = data['origin_file_name']
        
        converted_file = await convert_photo(file=data['photo'], origin_file_name=file_name, file_format=format_file)
            

    await message.answer_document(converted_file, allow_sending_without_reply=True)
        
    await state.finish()
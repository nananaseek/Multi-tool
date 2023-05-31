import logging

from aiogram import types
from aiogram.dispatcher import FSMContext


from ..app import dp
from ..states import AudioHandler, VideoHandler, PhotoHandler
from ..core.utils.file import save_file_to_memory, fix_file_name
from ..API import get_file_type
from ..API.convertor import convert_audio, convert_video, convert_photo
from bot_app.keyboards.inline.chosse_format_file import FileTypeKeyboard


@dp.message_handler(content_types=types.ContentType.VOICE, state=AudioHandler.file_handler)
@dp.message_handler(content_types=types.ContentType.AUDIO, state=AudioHandler.file_handler)
async def handle_audio_message(message: types.Message, state: FSMContext):
    try:
        global audio_type
        # Отримуємо аудіо, на яке відповідає користувач
        audio = message.audio
        media_type_audio = await get_file_type('audio')
        audio_type = FileTypeKeyboard(media_type_audio)
        audio_keyboard = await audio_type.get_keyboard()

        audio_values = message.audio.values
        # Зберігаємо аудіо в оперативну пам'ять
        audio_bytes = await save_file_to_memory(audio)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        await state.update_data(audio=audio_bytes.getvalue())
        await state.update_data(origin_file_name=audio.file_name)
        await state.update_data(title=audio.title)
        await state.update_data(performer=audio.performer)
        await state.update_data(duration=audio.duration)
        await state.update_data(thumb=audio.thumb)
        
        await message.answer('вибери формат на який хочеш конвертувати свій файл або напишіть свій формат ☺️',
                             reply_markup=audio_keyboard
                             )  
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
        
        converted_file = await convert_audio(
                                            file=data['audio'], 
                                            file_format=format_file, 
                                            origin_file_name=file_name
                                            )
    
    is_title = title if data['title'] else await fix_file_name(
                                                                original_file_name=file_name,
                                                                new_file_format=format_file
                                                                )
    
    await message.answer_audio(
                                converted_file, 
                                title=is_title, 
                                performer=performer,  
                                duration=duration, 
                                thumb=thumb, 
                                allow_sending_without_reply=True
                                )
    
    await state.finish()
    

@dp.callback_query_handler(lambda c: c.data in [type_name.lower() for type_name in audio_type.get_types()], state=AudioHandler.format_handler)
async def handle_audio_format(callback_query: types.CallbackQuery, state: FSMContext):
    selected_format = callback_query.data

    async with state.proxy() as data:
        
        file_name = data['origin_file_name']
        title = data['title']
        performer = data['performer']
        duration = data['duration']
        thumb = data['thumb']
        
        converted_file = await convert_audio(
                                            file=data['audio'], 
                                            file_format=selected_format, 
                                            origin_file_name=file_name
                                            )
        
    is_title = title if data['title'] else await fix_file_name(
                                                                original_file_name=file_name,
                                                                new_file_format=selected_format
                                                                )
    await callback_query.message.answer_audio(
                                converted_file, 
                                title=is_title, 
                                performer=performer,  
                                duration=duration, 
                                thumb=thumb, 
                                allow_sending_without_reply=True
                                )
    
    await state.finish()
    


"""
Функції для обробки відео повідоммлень
"""


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=VideoHandler.file_handler)
@dp.message_handler(content_types=types.ContentType.VIDEO, state=VideoHandler.file_handler)
async def handle_video_message(message: types.Message, state: FSMContext):
    try:
        global video_type
        media_type_video = await get_file_type('video')
        video_type = FileTypeKeyboard(media_type_video)
        video_keyboard = await video_type.get_keyboard()
        
        is_video = message.video
        # Отримуємо аудіо, на яке відповідає користувач
        video = is_video if is_video else message.document

        # Зберігаємо аудіо в оперативну пам'ять
        video_bytes = await save_file_to_memory(video)
        
        # Передаємо файл у контейнер сценарія що б потім можно було достати його з відти 
        await state.update_data(video=video_bytes.getvalue())
        if is_video:
            await state.update_data(duration=video.duration)
            await state.update_data(height=video.height)
            await state.update_data(width=video.width)
            await state.update_data(is_video=is_video)
        else:
            await state.update_data(is_video=is_video)
        
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️',
                             reply_markup=video_keyboard)  
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
    
    
@dp.callback_query_handler(lambda c: c.data in [type_name.lower() for type_name in video_type.get_types()], state=VideoHandler.format_handler)
async def handle_audio_format(callback_query: types.CallbackQuery, state: FSMContext):
    selected_format = callback_query.data
    
    async with state.proxy() as data:
        
        is_video = data['is_video']
        
        if is_video:
            duration = data['duration']
            height = data['height']
            width = data['width']
        
        converted_file = await convert_video(file=data['video'], file_format=selected_format)
            
    if is_video:
        await callback_query.message.answer_video(converted_file,  duration=duration, height=height, width=width, allow_sending_without_reply=True )
    else:
        await callback_query.message.answer_video(converted_file, allow_sending_without_reply=True )
        
    await state.finish()
    
    
"""
Функції для обробки фотографій
"""

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=PhotoHandler.file_handler)
async def handle_photo_message(message: types.Message, state: FSMContext):
    try:
        global photo_type
        media_type_photo = await get_file_type('photo')
        photo_type = FileTypeKeyboard(media_type_photo)
        photo_keyboard = await photo_type.get_keyboard()
        
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
        
        await message.answer('напиши формат на який хочеш конвертувати свій файл ☺️', 
                            reply_markup= photo_keyboard)  
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
    
    
@dp.callback_query_handler(lambda c: c.data in [type_name.lower() for type_name in photo_type.get_types()], state=PhotoHandler.format_handler)
async def handle_audio_format(callback_query: types.CallbackQuery, state: FSMContext):
    selected_format = callback_query.data
    
    
    async with state.proxy() as data:
        
        file_name = data['origin_file_name']
        
        converted_file = await convert_photo(file=data['photo'], origin_file_name=file_name, file_format=selected_format)
            

    await callback_query.message.answer_document(converted_file, allow_sending_without_reply=True)
        
    await state.finish()
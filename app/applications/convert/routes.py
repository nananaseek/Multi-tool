import os
import asyncio

from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, UploadFile, Response
from fastapi.responses import StreamingResponse, FileResponse
from app.settings.config import settings

from app.core.utils import delete_file_after_delay, \
    create_folder, \
    save_file, \
    check_file_exists, \
    get_audio_media_type, \
    get_image_media_type, \
    get_video_media_type


from app.applications.convert.utils import convert_audio, \
    convert_image, \
    convert_video


import logging
logger = logging.getLogger(__name__)

router = APIRouter()

temp_folder = settings.TEMP_FOLDER

    
@router.post("/audio", status_code=200, tags=['Convertor'])
async def converting_audio(file: UploadFile = File(...), file_format: Optional[str] = "mp3"):
    """
    Конвертує вхідний аудіофайл у вказаний формат та повертає вихідний аудіофайл.

    Args:
    - file: UploadFile = File(...): вхідний аудіофайл
    - file_format: Optional[str] = "mp3": формат вихідного аудіофайлу (за замовчуванням 'mp3')

    :return: вихідний аудіофайл у вказаному форматі
    :raises HTTPException: якщо сталася помилка при конвертуванні файлу
    """

    # file_location - шлях до файлу з назвою файла.
    file_location = f"{temp_folder}{file.filename}"
    
    # name_file - назва файла без шляху до нього.
    name_file = file_location.split("/")[-1]

    # name_without_extension - назва файлу без розширення.
    name_without_extension = os.path.splitext(name_file)[0]

    # conv_file_name - назва файлу після конвертації з розширенням.
    conv_file_name = f'{name_without_extension}.{file_format}'

    # full_path_converted_file - повний шлях до файлу після конвертації з розширенням.
    full_path_converted_file = f'{temp_folder}{conv_file_name}'
  

    try:
        # Перевіряємо, чи існує папка temp і створюємо її, якщо не існує
        await create_folder(temp_folder)
            
        # Зберігаємо файл у тимчасову папку
        if not await check_file_exists(file_location):
            await save_file(file=file, file_location=file_location)

        if not await check_file_exists(full_path_converted_file):
            converted_file = await convert_audio(
                                input_file=file_location,
                                output_format=file_format,
                                temp_folder=temp_folder,
                                name_file=name_without_extension)
        else:
            converted_file = full_path_converted_file
                
        # Включаємо автовидалення файлів користувача після того як пройшов деякий час
        task = asyncio.create_task(delete_file_after_delay(
                orig_file_path=file_location, 
                conv_file_path=full_path_converted_file
                ))
        

        return FileResponse(
            path=converted_file, 
            filename=conv_file_name, 
            media_type= await get_audio_media_type(file_format)
            )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/picture", status_code=200, tags=['Convertor'])
async def converting_picture(file: UploadFile = File(...), file_format: Optional[str] = "jpeg"):
    """
    Конвертує вхідний аудіофайл у вказаний формат та повертає вихідний аудіофайл.

    Args:
    - file: UploadFile = File(...): вхідний аудіофайл
    - file_format: Optional[str] = "jpeg": формат вихідного аудіофайлу (за замовчуванням 'jpeg')

    :return: вихідний аудіофайл у вказаному форматі
    :raises HTTPException: якщо сталася помилка при конвертуванні файлу
    """

    # file_location - шлях до файлу з назвою файла.
    file_location = f"{temp_folder}{file.filename}"
    
    # name_file - назва файла без шляху до нього.
    name_file = file_location.split("/")[-1]

    # name_without_extension - назва файлу без розширення.
    name_without_extension = os.path.splitext(name_file)[0]

    # conv_file_name - назва файлу після конвертації з розширенням.
    conv_file_name = f'{name_without_extension}.{file_format}'

    # full_path_converted_file - повний шлях до файлу після конвертації з розширенням.
    full_path_converted_file = f'{temp_folder}{conv_file_name}'

    
    
    try:
        # Перевіряємо, чи існує папка temp і створюємо її, якщо не існує
        await create_folder(temp_folder)
            
        # Зберігаємо файл у тимчасову папку
        if not await check_file_exists(file_location):
            await save_file(file=file, file_location=file_location)

        if not await check_file_exists(full_path_converted_file):
            converted_file = await convert_image(input_filename=file_location, output_format=file_format)
        else:
            converted_file = full_path_converted_file
            
        # Включаємо автовидалення файлів користувача після того як пройшов деякий час
        task = asyncio.create_task(delete_file_after_delay(
                orig_file_path=file_location, 
                conv_file_path=full_path_converted_file
                ))
        

        return FileResponse(
            path=converted_file, 
            filename=conv_file_name, 
            media_type = await get_image_media_type(file_format)
            )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/video", status_code=200, tags=['Convertor'])
async def converting_video(file: UploadFile = File(...), file_format: Optional[str] = ""):
    """
    Конвертує вхідний відеофайл у вказаний формат та повертає вихідний відеофайл.

    Args:
    - file: UploadFile = File(...): вхідний відеофайл
    - file_format: Optional[str] = "jpeg": формат вихідного відеофайлу

    :return: вихідний відеофайл у вказаному форматі
    :raises HTTPException: якщо сталася помилка при конвертуванні файлу
    """

    # file_location - шлях до файлу з назвою файла.
    file_location = f"{temp_folder}{file.filename}"
    
    # name_file - назва файла без шляху до нього.
    name_file = file_location.split("/")[-1]

    # name_without_extension - назва файлу без розширення.
    name_without_extension = os.path.splitext(name_file)[0]

    # conv_file_name - назва файлу після конвертації з розширенням.
    conv_file_name = f'{name_without_extension}.{file_format}'

    # full_path_converted_file - повний шлях до файлу після конвертації з розширенням.
    full_path_converted_file = f'{temp_folder}{conv_file_name}'

    
    
    try:
        # Перевіряємо, чи існує папка temp і створюємо її, якщо не існує
        await create_folder(temp_folder)
            
        # Зберігаємо файл у тимчасову папку
        if not await check_file_exists(file_location):
            await save_file(file=file, file_location=file_location)

        if not await check_file_exists(full_path_converted_file):
            converted_file = await convert_video(
                                    input_filename=file_location, 
                                    output_format=file_format,
                                    temp_folder=temp_folder,
                                    name_file=name_without_extension
                                    )
        else:
            converted_file = full_path_converted_file
            
        # Включаємо автовидалення файлів користувача після того як пройшов деякий час
        task = asyncio.create_task(delete_file_after_delay(
                orig_file_path=file_location, 
                conv_file_path=full_path_converted_file
                ))
        

        return FileResponse(
            path=converted_file, 
            filename=conv_file_name, 
            media_type = await get_video_media_type(file_format)
            )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

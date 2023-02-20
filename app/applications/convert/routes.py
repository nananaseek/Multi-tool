import os
import io
import aiofiles
import asyncio

from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, UploadFile, Response
from fastapi.responses import StreamingResponse, FileResponse
from app.settings.config import settings

from app.applications.convert.utils import convert_audio,\
    delete_file_after_delay

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/audio", status_code=200, tags=['Convertor'])
async def convert(file: UploadFile = File(...), format: Optional[str] = "mp3"):
    # try:
        # Перевіряємо, чи існує папка temp і створюємо її, якщо не існує
        temp_folder = f"{settings.BASE_DIR}/temp/"
        if not os.path.isdir(temp_folder):
            os.makedirs(temp_folder)
            
        # Зберігаємо файл у тимчасову папку
        file_location = f"{settings.BASE_DIR}/temp/{file.filename}"
        content = file.file.read()
        with open(file_location, 'wb') as buffer:
            buffer.write(content)

        name_file = file_location.split("/")[-1]
        name_without_extension = os.path.splitext(name_file)[0] 
        converted_file = await convert_audio(
                            input_file=file_location,
                            output_format=format,
                            temp_folder=temp_folder,
                            name_file=name_without_extension)
        
        conv_file_name = f'{name_without_extension}.{format}'
        full_path_converted_file = f'{settings.BASE_DIR}/temp/{conv_file_name}'
        
        # Включаємо автовидалення файлів користувача після того як пройшов деякий час
        task = asyncio.create_task(delete_file_after_delay(
                orig_file_path=file_location, 
                conv_file_path=full_path_converted_file
                ))
        

        return FileResponse(
            path=converted_file, 
            filename=conv_file_name, 
            media_type='audio/basic' 
            )
    # except Exception as e:
        # raise HTTPException(status_code=500, detail=str(e))
        
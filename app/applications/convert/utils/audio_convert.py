import os
import asyncio
import aiofiles
import logging
from pydub import AudioSegment
from pydub.utils import mediainfo
from fastapi import HTTPException, UploadFile
from pydub.exceptions import CouldntDecodeError

from app.settings.config import settings


# конвертування аудіо файлів
async def is_convertible_to_audio(file_path: str) -> bool:
    """
    Перевіряє, чи може бібліотека Pydub конвертувати файл.

    :param file_path: шлях до файлу
    :return: True, якщо файл можна конвертувати, False в іншому випадку
    """
    try:
        loop = asyncio.get_running_loop()
        mediainfo_data = await loop.run_in_executor(None, mediainfo, file_path)
    except CouldntDecodeError as e:
        logging.error(f'File: {file_path} get error, {e}')
        return False

    return mediainfo_data.get("codec_type") == "audio"

async def convert_audio(input_file: str, output_format: str, temp_folder: str, name_file: str) -> str:
    """
    Конвертує аудіофайл у вказаний формат та шлях до файлу.

    :param input_file: шлях до вхідного файлу
    :param output_format: формат вихідного файлу
    :return: шлях до вихідного аудіофайлу
    """

    input_format = input_file.split(".")[-1]
    if await is_convertible_to_audio(file_path=input_file):
        audio = AudioSegment.from_file(input_file, format=input_format)
        output_file = f"{temp_folder}{name_file}.{output_format}"
        audio.export(output_file, format=output_format)

    return output_file
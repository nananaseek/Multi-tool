import os
import asyncio
import aiofiles
import logging
from pydub import AudioSegment
from pydub.utils import mediainfo
from fastapi import HTTPException
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
        logging.info(f'File: {file_path} get error, {e}')
        return False

    return mediainfo_data.get("codec_type") == "audio"

async def convert_audio(input_file: str, output_format: str, temp_folder: str, name_file: str) -> str:
    """
    Конвертує аудіофайл у вказаний формат та повертає байти.

    :param input_file: шлях до вхідного файлу
    :param output_format: формат вихідного файлу
    :return: байти вихідного аудіофайлу
    """

    input_format = input_file.split(".")[-1]
    if await is_convertible_to_audio(file_path=input_file):
        audio = AudioSegment.from_file(input_file, format=input_format)
        output_file = f"{temp_folder}{name_file}.{output_format}"
        audio.export(output_file, format=output_format)

    return output_file


# Загальні функції
async def delete_file_after_delay(orig_file_path: str, conv_file_path: str, delay: int = 10) -> None: 
    """
    Асинхронна функція, що видаляє файл з затримкою.

    Args:
        orig_file_path (str): Шлях до оригінального файлу, який потрібно видалити.
        conv_file_path (str): Шлях до конвертованого файлу, який потрібно видалити.
        delay (int): Затримка в секундах перед видаленням файлу.

    Returns:
        None

    """
    try:
        # чекаємо вказану кількість секунд
        await asyncio.sleep(delay)

        # видаляємо файл з диску, тільки якщо він існує
        if os.path.exists(orig_file_path):
            os.remove(orig_file_path)
            logging.info(f"File {orig_file_path} has been deleted.")
        if os.path.exists(conv_file_path):
            os.remove(conv_file_path)
            logging.info(f"File {conv_file_path} has been deleted.")

    except Exception as e:
        logging.info(f"Error deleting file: {e}")

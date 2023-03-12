import os
import asyncio
import logging

from fastapi import HTTPException, UploadFile


async def delete_file_after_delay(orig_file_path: str, conv_file_path: str, delay: int = 60) -> None: 
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
        

async def create_folder(temp_folder: str) -> bool:
    """
    create_folder() це асинхронна функція, яка створює папку "temp" в директорії
    Якщо така папка вже створена, то створення не виконується.
    Функція повертає строку, яка містить розміщення папки "temp".
    """
    
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
        logging.info('Folder temp/ created')
    
    return True


async def check_file_exists(file_location: str) -> bool:
    """
    Функція для перевірки чи файл існує.

    Args:
        file_location: str - місце збереження файлу.

    Returns:
        bool: повертає True якщо файл існує, False - якщо ні.

    Функція використовує метод os.path.exists() для перевірки чи існує файл.
    """
    if os.path.exists(file_location):
        logging.info(f"Файл {file_location} існує.")
        return True
    else:
        logging.warning(f"Файл {file_location} не існує.")
        return False


async def save_file(file: UploadFile, file_location: str) -> bool:
    """
    Функція для створення файлу.

    Args:
        file: UploadFile - назва файлу.
        file_location: str - місце збереження файлу.

    Returns:
        bool: повертає True, якщо файл було успішно збережено, False - якщо ні.

    Функція використовує check_file_exists() для перевірки чи файл існує, 
    file.file.read() для створення контенту, який потрібно записати, 
    тоді створює buffer, який використовує open() та write() для запису у файл контенту.
    """

    content = file.file.read()
    with open(file_location, 'wb') as buffer:
        buffer.write(content)
    return True

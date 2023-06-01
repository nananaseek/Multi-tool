from aiogram.types import File

from io import BytesIO

from ...app import bot


async def save_file_to_memory(file: File) -> BytesIO:
    """
    Зберігає вхідний файл у пам'ять (об'єкт BytesIO).

    Args:
        file (File): Вхідний файл, який потрібно зберегти.

    Returns:
        BytesIO: Об'єкт BytesIO, що містить дані з вхідного файлу.

    """
    file_bytes = BytesIO()  # Створення об'єкту BytesIO для збереження файлу в пам'яті
    await file.download(destination_file=file_bytes)  # Завантаження файлу в об'єкт BytesIO
    file_bytes.seek(0)  # Встановлення позиції зчитування на початок файлу
    return file_bytes  # Повернення об'єкту BytesIO з даними з вхідного файлу



async def download_and_send_voice_message(file_id: str) -> BytesIO:
    """
    Скачує голосове повідомлення за заданим ідентифікатором файлу і повертає його дані у форматі BytesIO.

    Аргументи:
    - file_id (str): Ідентифікатор файлу голосового повідомлення.

    Повертає:
    BytesIO: Дані голосового повідомлення у форматі BytesIO.

    Виключення:
    - BotAPIError: Якщо сталася помилка під час отримання файлу голосового повідомлення.

    """
    
    # Скачування голосового повідомлення за заданим ідентифікатором файлу
    file = await bot.get_file(file_id)

    # Збереження голосового повідомлення в пам'ять у форматі BytesIO
    voice_data = await save_file_to_memory(file=file)

    # Повернення даних голосового повідомлення
    return voice_data




async def download_and_send_video_note(file_id: str) -> BytesIO:
    """
    Завантажує та надсилає відео-повідомлення за його ідентифікатором.

    Args:
        file_id (str): Ідентифікатор відео-повідомлення.

    Returns:
        BytesIO: Об'єкт BytesIO, що містить дані відео-повідомлення.

    Raises:
        Жодного винятку не генерується.

    """
    
    # Скачування голосового повідомлення
    file = await bot.get_file(file_id)
    video_note_data = await save_file_to_memory(file=file)

    # Відправка голосового повідомлення назад у чат
    return video_note_data


async def fix_file_name(original_file_name: str, new_file_format: str) -> str:
    """
    Оновлює формат назви файлу шляхом заміни розширення на нове розширення.

    Args:
    - original_file_name: str: початкова назва файлу
    - new_file_format: str: новий формат розширення файлу

    Returns:
    - str: оновлена назва файлу з новим розширенням

    Example:
    >>> await fix_file_name("audio.wav", "mp3")
    "audio.mp3"
    """

    file_name_without_format = original_file_name.split('.')[0]
    file_name_update_format = f'{file_name_without_format}.{new_file_format}'

    return file_name_update_format

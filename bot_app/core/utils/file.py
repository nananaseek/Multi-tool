from aiogram.types import File

from io import BytesIO

from ...app import bot


async def save_file_to_memory(file: File) -> BytesIO:
    file_bytes = BytesIO()
    await file.download(destination_file=file_bytes)
    file_bytes.seek(0)  # Переміщуємо покажчик в початок файлу
    return file_bytes


async def download_and_send_voice_message(file_id: str) -> BytesIO:
    # Скачування голосового повідомлення
    file = await bot.get_file(file_id)
    voice_data = await save_file_to_memory(file=file)

    # Відправка голосового повідомлення назад у чат
    return voice_data


async def download_and_send_video_note(file_id: str) -> BytesIO:
    # Скачування голосового повідомлення
    file = await bot.get_file(file_id)
    video_note_data = await save_file_to_memory(file=file)

    # Відправка голосового повідомлення назад у чат
    return video_note_data
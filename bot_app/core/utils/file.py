from aiogram.types import File

from io import BytesIO


async def save_file_to_memory(file: File) -> BytesIO:
    file_bytes = BytesIO()
    await file.download(destination_file=file_bytes)
    file_bytes.seek(0)  # Переміщуємо покажчик в початок файлу
    return file_bytes
import aiohttp

from ...settings.conf import settings



async def convert_audio(file: bytes, file_format: str, origin_file_name: str) -> bytes:
    """
    Конвертує вхідний аудіофайл у вказаний формат за допомогою веб-сервісу.

    Args:
        file (bytes): Вхідний аудіофайл, представлений у вигляді байтового рядка.
        file_format (str): Формат вихідного аудіофайлу, який буде використовуватись для конвертації.
        origin_file_name (str): Початкове ім'я файлу, яке буде використовуватись для конвертації.

    Returns:
        bytes: Конвертований аудіофайл у вигляді байтового рядка.

    Raises:
        Exception: Якщо сталася помилка під час конвертації аудіофайлу.

    """
    payload = {
        'extra_file_name': origin_file_name,
        'file_format': file_format
    }
    data = {'file': file}

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.AUDIO_ENDPOINT, data=data, params=payload) as response:
            processed_audio = await response.content.read()

    return processed_audio

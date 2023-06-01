import aiohttp

from ...settings.conf import settings



async def convert_photo(file: bytes, file_format: str, origin_file_name: str) -> bytes:
    """
    Виконує конвертацію фото у вказаний формат за допомогою віддаленого сервісу.

    Args:
        file (bytes): Байтове представлення вхідного фото.
        file_format (str): Формат вихідного фото, який буде використовуватись під час конвертації.
        origin_file_name (str): Оригінальне ім'я файла фото.

    Returns:
        bytes: Байтове представлення сконвертованого фото.

    Raises:
        HTTPException: Якщо сталася помилка при виконанні запиту до віддаленого сервісу.

    """
    payload = {'extra_file_name': origin_file_name, 'file_format': file_format}
    data = {'file': file}

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.PHOTO_ENDPOINT, data=data, params=payload) as response:
            processed_photo = await response.content.read()

    return processed_photo

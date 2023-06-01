import aiohttp

from ...settings.conf import settings



async def convert_video(file: bytes, file_format: str) -> bytes:
    """
    Відправляє відеофайл на сервер для конвертації у вказаний формат і повертає оброблений відеофайл.

    Args:
        file: bytes: байтове представлення вхідного відеофайлу
        file_format: str: формат вихідного відеофайлу

    Returns:
        bytes: байтове представлення обробленого відеофайлу

    Raises:
        HTTPException: Якщо сталася помилка під час конвертації або отримання відповіді з сервера
    """
    payload = {
        'file_format': file_format
    }
    data = {'file': file}

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.VIDEO_ENDPOINT, data=data, params=payload) as response:
            processed_video = await response.content.read()

    return processed_video

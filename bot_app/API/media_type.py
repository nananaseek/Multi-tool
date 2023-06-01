import aiohttp

from bot_app.settings.conf import settings


async def get_file_type(file_type: str) -> dict:
    """
    Отримує тип файлу з вказаного ресурсу API залежно від переданого параметру `file_type`.

    Args:
    - file_type (str): Тип файлу. Припустимі значення: 'audio', 'video', 'photo'.

    Returns:
    - file_type (dict): Словник, що містить інформацію про тип файлу, отриману з ресурсу API.

    Raises:
    - None

    """
    match file_type:
        case 'audio':
            endpoint = settings.AUDIO_TYPE_ENDPOINT
        case 'video':
            endpoint = settings.VIDEO_TYPE_ENDPOINT
        case 'photo':
            endpoint = settings.PHOTO_TYPE_ENDPOINT

    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint) as response:
            file_type = await response.json()

    return file_type

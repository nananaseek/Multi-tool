import aiohttp

from bot_app.settings.conf import settings


async def get_file_type(file_type: str):
    
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
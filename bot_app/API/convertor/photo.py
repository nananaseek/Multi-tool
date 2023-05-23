import aiohttp

from ...settings.conf import settings



async def convert_photo(file: bytes, file_format: str, origin_file_name: str):
    payload = {'extra_file_name': origin_file_name,
                'file_format': file_format
                }
    data = {'file': file}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(settings.PHOTO_ENDPOINT,data=data, params=payload) as response:
            processed_video = await response.content.read()

    return processed_video

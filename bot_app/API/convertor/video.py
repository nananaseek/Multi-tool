import aiohttp

from ...settings.conf import settings



async def convert_video(file: bytes, file_format: str):
    payload = {
                'file_format': file_format
                }
    data = {'file': file}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(settings.VIDEO_ENDPOINT,data=data, params=payload) as response:
            processed_video = await response.content.read()

    return processed_video

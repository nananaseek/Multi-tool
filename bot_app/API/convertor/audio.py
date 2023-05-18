from ..base_api import ApiClient
from ...settings.conf import AUDIO_CONV_ENDPOINT


async def convert_audio(file: bytes, file_format: str):
    payload = {'file_format': file_format}

    async with ApiClient() as client:
        response = await client.post(AUDIO_CONV_ENDPOINT, payload)

    if response.get('success'):
        return {'message': 'Conversion successful'}
    else:
        return {'message': 'Conversion failed'}
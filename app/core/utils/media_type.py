async def get_image_media_type (file_format: str) -> str:
    """
    Функція повертає media type відповідно до формату файлу.

    Args:
        file_format: str - формат файлу.

    Returns:
        str - media type.

    Raises:
        ValueError: якщо формат файлу невідомий.
    """
    match file_format.split():
        case ['jpeg' | 'jpg']:
            return 'image/jpeg'
        case ['png']:
            return 'image/png'
        case ['gif']:
            return 'image/gif'
        case ['svg'], 'xml':
            return 'image/svg+xml'
        case ['tiff']:
            return 'image/tiff'
        case ['icon']:
            return 'image/vnd.microsoft.icon'
        case ['webp' | 'bmp' | 'ico']:
            return f'image/{file_format}'
        case _:
            raise ValueError(f'Unknown file format: {file_format}')


async def get_audio_media_type(file_format: str) -> str:
    """Повертає media type для аудіо формату

    Args:
        file_format (str): Формат аудіо файлу.

    Returns:
        str: Media type аудіо файлу.
    """
    match file_format.lower():
        case 'mp3':
            return 'audio/mpeg'
        case 'wav':
            return 'audio/wav'
        case 'ogg':
            return 'audio/ogg'
        case 'flac':
            return 'audio/flac'
        case 'aac':
            return 'audio/aac'
        case 'wma':
            return 'audio/x-ms-wma'
        case 'aiff':
            return 'audio/aiff'
        case 'au':
            return 'audio/basic'
        case 'm4a':
            return 'audio/mp4'
        case 'opus':
            return 'audio/opus'
        case _:
            return 'application/octet-stream'

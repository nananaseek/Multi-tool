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
    match file_format.lower().split():
        case ['jpeg' | 'jpg']:
            return 'image/jpeg'
        case ['png']:
            return 'image/png'
        case ['gif']:
            return 'image/gif'
        case ['svg' | 'xml']:
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
    """
    Функція повертає media type відповідно до формату файлу.

    Args:
        file_format: str - формат файлу.

    Returns:
        str - media type.

    Raises:
        ValueError: якщо формат файлу невідомий.
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

async def get_video_media_type (file_format: str) -> str:
    """
    Функція повертає media type відповідно до формату файлу.

    Args:
        file_format: str - формат файлу.

    Returns:
        str - media type.

    Raises:
        ValueError: якщо формат файлу невідомий.
    """
    match file_format.lower().split():
        case ["mpg" | "mpeg" | "mp1" | "mp2" | "mp3" | "m1v" | "mpv" | "m1a" | "m2a"  | "mpa"]:
            return 'video/mpeg'
        case ['mp4' | "m4a" | "m4v" | "f4v" | "f4a" | "m4b" | "m4r" | "f4b" | "mov"]:
            return 'video/mp4'
        case ['ogg' | 'ogv' | 'oga' | 'ogx' | 'spx' | 'opus' ]:
            return 'video/ogg'
        case ['webm']:
            return 'video/webm'
        case ['wmv']:
            return 'video/x-ms-wmv'
        case ['avi']:
            return 'video/x-msvideo'
        case ['3gpp' | '3gp']:
            return 'video/3gpp'
        case ['3gpp2' | '3g2']:
            return 'video/3gpp2'
        case _:
            raise ValueError(f'Unknown file format: {file_format}')
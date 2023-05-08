import moviepy.editor as mp
import logging
import os

from app.settings.config import settings


async def convert_video(input_filename: str, output_format: str, temp_folder: str, name_file: str) -> str:
    """
    Функція, що конвертує файл в розширення output_format та повертає шлях до результуючого файлу
    :param input_filename: шлях до файлу
    :param output_format: розширення, в яке потрібно конвертувати
    :return: шлях до конвертованого файла
    """
    try:
        video = mp.VideoFileClip(input_filename)
        output_file = f"{temp_folder}{name_file}.{output_format}"
        video.write_videofile(output_file, codec=(lambda output_format: {
                                'mp4': 'libx264',
                                'ogv': 'libtheora',
                                'webm': 'libvpx',
                                'ogg': 'libtheora',
                                'mp3': 'pcm_s16le',
                                'wav': 'libvorbis',
                                'm4a': 'libfdk_aac',
                            }.get(format, 'libx264'))(output_format))
        logging.info('Відео файл було конвертовано успішно')
        
        return output_file
    
    except Exception as e:
        logging.error(f'Файл {input_filename} не був конвертований, detils: {e}')
        return None
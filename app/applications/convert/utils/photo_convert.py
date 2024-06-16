import logging
from PIL import Image

async def can_convert_to_format(file_path: str, target_format: str) -> bool:
    """
    Функція перевіряє, чи можливе конвертування файлу у вказаний формат.

    :param file_path: Шлях до файлу зображення
    :param target_format: Формат, до якого потрібно конвертувати зображення
    :return: True, якщо конвертування можливе, інакше False
    """
    try:
        with Image.open(file_path) as img:
            if img.format.lower() == target_format.lower():
                logging.info("Файл уже має вказаний формат.")
                return True
            else:
                return True
    except IOError:
        logging.error(f"Не вдалося відкрити файл {file_path}")
        return False

async def convert_image(input_filename: str, output_format: str) -> str:
    """
    Функція, яка конвертує зображення з одного формату в інший

    :param input_filename: Шлях до файлу зображення
    :param output_format: Розширення, до якого має бути конвертовано зображення
    :return: Шлях до нового файлу зображення
    """
    if not await can_convert_to_format(input_filename, output_format):
        logging.warning(f"Файл {input_filename} не може бути конвертований до формату {output_format}.")
        return None

    try:
        with Image.open(input_filename) as img:
            new_file_path = input_filename.replace(img.format, output_format)
            img.save(new_file_path)
            logging.info(f"Зображення успішно конвертовано до формату {output_format}.")
            return new_file_path
    except IOError:
        logging.error(f"Не вдалося відкрити або зберегти файл {input_filename}")
        return None
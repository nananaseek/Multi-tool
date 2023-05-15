from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def generate_inline_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    audio_button = InlineKeyboardButton("Аудіо", callback_data="audio")
    video_button = InlineKeyboardButton("Відео", callback_data="video")
    photo_button = InlineKeyboardButton("Фото", callback_data="photo")
    
    keyboard.add(audio_button, video_button)
    keyboard.add(photo_button)
    
    return keyboard

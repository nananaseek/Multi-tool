from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def chosse_format_file():
    """
    Клавіатура для вибору типу скидуваємого формату 
    """
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    audio_button = InlineKeyboardButton("Аудіо", callback_data="audio")
    video_button = InlineKeyboardButton("Відео", callback_data="video")
    photo_button = InlineKeyboardButton("Фото", callback_data="photo")
    
    keyboard.add(audio_button, video_button)
    keyboard.add(photo_button)
    
    return keyboard


class FileTypeKeyboard:
    def __init__(self, file_type: list):
        self.type_list = file_type
    
    async def get_keyboard(self):
        keyboard = InlineKeyboardMarkup(row_width=2)
            
        buttons = [
            InlineKeyboardButton(text=type_name, callback_data=type_name.lower()) 
            for type_name in self.type_list
        ]
        keyboard.add(*buttons)
        return keyboard
    
    def get_types(self):
        return self.type_list



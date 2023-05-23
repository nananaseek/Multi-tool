from aiogram.dispatcher.filters.state import State, StatesGroup

class AudioHandler(StatesGroup):
    file_handler = State()
    format_handler = State()

class VideoHandler(StatesGroup):
    file_handler = State()
    format_handler = State()

class PhotoHandler(StatesGroup):
    file_handler = State()
    format_handler = State()

class VoiceAndVideo(StatesGroup):
    file_handler = State()
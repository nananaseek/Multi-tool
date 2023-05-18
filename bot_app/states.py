from aiogram.dispatcher.filters.state import State, StatesGroup

class FileHandlerGroup(StatesGroup):
    file_handler = State()
    format_handler = State()
    file_upload = State()

import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from ..app import dp
from ..settings.conf import settings

if settings.DEBUG:
    @dp.message_handler(state='*', commands='state')
    @dp.message_handler(Text(equals='state', ignore_case=True), state='*')
    async def state_handler(message: types.Message, state: FSMContext):
        state_info = f'Стан бота: {await state.get_state()}'
        state_data = f'У стані бота така інформація: {await state.get_data()}'
        debug_state_info = f'{state_info}\n{state_data}'
        
        logging.debug(debug_state_info)
        await message.answer(debug_state_info)
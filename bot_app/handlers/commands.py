from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import logging

from ..app import dp
from ..core.message import *
from ..keyboards.inline import *
from ..states import VoiceAndVideo


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(START_MESS,
                         parse_mode='HTML',
                        )

@dp.message_handler(commands='convert')
async def convert_mess(message: types.Message):
    await message.answer(CONVERT_MESSAGE,
                         reply_markup=chosse_format_file())

@dp.message_handler(commands='download')
async def convert_mess(message: types.Message, state: FSMContext):
    await message.answer(DOWNLOAD_MESSAGE)
    await VoiceAndVideo.file_handler.set()
    
# Функція для виходу зі сценарія при команді /cancel
# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())
        
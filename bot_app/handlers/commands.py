from aiogram import types
from aiogram.dispatcher import FSMContext

from ..app import *
from ..message import *
from ..keyboards.inline import *
from ..utils import *


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(START_MESS,
                         parse_mode='HTML',
                         reply_markup=generate_inline_keyboard())

@dp.message_handler(commands='cancel', state='*')
async def cancel_command_handler(message: types.Message, state: FSMContext):
    await cancel_handler(message, state)
    await message.answer('Ви відмінили операцію')
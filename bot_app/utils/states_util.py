from aiogram import types
from aiogram.dispatcher import FSMContext


# Функція для виходу зі сценарія при команді /cancel
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return 

    # Очищаємо стан
    await state.finish()

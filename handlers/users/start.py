from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import (
    start_buttons,
) 
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalomu alekum, <b  style='font-weigth:700'>{message.from_user.full_name}</b>! \n UstozShogirt kanalining rasmiy botiga xush kelibsiz!</b> \n\n /help buyrug'i orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=start_buttons)

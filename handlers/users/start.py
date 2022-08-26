from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import (
    start_buttons,
) 
from loader import dp, base, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    lname = message.from_user.first_name
    username = message.from_user.username
    tg_id = message.from_user.id
    try:
        base.foydalanuvchi_qoshish(name=name, username=username, tg_id=tg_id, lastname=lname)
    except Exception:
        pass

    await message.answer(f"<b>Assalomu alekum, <b  style='font-weigth:700'>{message.from_user.full_name}</b>! \n UstozShogirt kanalining rasmiy botiga xush kelibsiz!</b> \n\n /help buyrug'i orqali nimalarga qodir ekanligimni bilib oling!", reply_markup=start_buttons)

@dp.message_handler(commands='reklama', chat_id='1603330179')
async def bot_univer(message: types.Message):
    all_users = base.select_users()
    for user in all_users:
        tg_id = user[4]

        text = "Bot yordamida barcha foydalanuvchilarga reklama yuborildi, sinov uchun albatta"
        await bot.send_message(chat_id=tg_id, text=text)

@dp.message_handler(commands='users')
async def univer(message: types.Message):
    users_count = base.foydalanuvchilar_soni()[0]
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=f"Foydalanuvchilar soni: {users_count} ta")
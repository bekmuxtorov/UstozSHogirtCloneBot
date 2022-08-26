from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (f"@UstozShogirt kanalining norasmiy clone boti. O'rganish va o'rganganlarimni takrorlash uchun bajarilgan ish, bundan hech qanday moddiy manfaat ko'zlanmagan")
    
    await message.answer(text=text)

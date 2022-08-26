from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from keyboards.inline.inline_buttons import azolik_buttons
from aiogram.types import CallbackQuery

from data.config import kanallar
from utils.tekshirish import checking
from loader import bot, dp

class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self, xabar:types.Update, data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return 

        matn = 'Quydagi kanalga a\'zo boling:'
        dastlabki_holat = True
        for kanal in kanallar:
            holat = await checking(user_id=user_id, kanal=kanal)
            dastlabki_holat *= holat

            kanal = await bot.get_chat(kanal)
            if not holat:
                link = await kanal.export_invite_link()
                matn+=(f"\n👉 <b><a href='{link}'>{kanal.title}</a></b>")
        
        if not dastlabki_holat:
            await xabar.message.reply(matn, disable_web_page_preview=True)
            raise CancelHandler()
        

@dp.callback_query_handler(text='tekshirish')
async def tekshirish(matn: CallbackQuery):
    await matn.message.answer(text='Ajoyib!\n\nBotdan foydalanishingiz mumkin.')

        
from aiogram import types
from states.holatlar import Holatlar
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import tasdiqlash_buttons,start_buttons
from .foydali_funksiyalar import (
    jonatish,
    )
from data.config import kanallar

from loader import dp,bot

@dp.message_handler(text='Shogirt kerak')
async def bot_echo(message: types.Message):
    text = """<b>Shogirt topish uchun ariza berish</b> \n\n Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering.
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
    await message.answer(text=text)
    await message.answer(text='<b>Ism familiyangizni kiriting?</b>')
    await Holatlar.shogirt_ism_holati.set()


@dp.message_handler(state=Holatlar.shogirt_ism_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data({"ism": ism})
    text = "🕑 <b>Yosh:</b>\n\nYoshingizni kiriting?\nMasalan, 19"
    await message.answer(text=text)
    await Holatlar.shogirt_yosh_holati.set()

@dp.message_handler(state=Holatlar.shogirt_yosh_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"yosh": yosh})
    text = "📚<b>Texnalogiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n <i>Java, C++, C#</i>"
    await message.answer(text=text)
    await Holatlar.shogirt_texnalogiya_holati.set()

@dp.message_handler(state=Holatlar.shogirt_texnalogiya_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    texnalogiya = message.text
    await state.update_data({"texnalogiya": texnalogiya})
    text = "📞<b>Aloqa:</b>\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67"
    await message.answer(text=text)
    await Holatlar.shogirt_aloqa_holati.set()


@dp.message_handler(state=Holatlar.shogirt_aloqa_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data({"aloqa": aloqa})
    text = "🌐<b>Hudud:</b>\n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting."
    await message.answer(text=text)
    await Holatlar.shogirt_hudud_holati.set()


@dp.message_handler(state=Holatlar.shogirt_hudud_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data({"hudud": hudud})
    text = "💰<b>Narxi:</b>\n\nTo'lov qilasizmi yoki Tekinmi? \nKerak bo`lsa, Summani kiriting?"
    await message.answer(text=text)
    await Holatlar.shogirt_narx_holati.set()

@dp.message_handler(state=Holatlar.shogirt_narx_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    narx = message.text
    await state.update_data({"narx": narx})
    text = "👨🏻‍💻<b>Kasbi:</b>\n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba"
    await message.answer(text=text)

    await Holatlar.shogirt_kasb_holati.set()

@dp.message_handler(state=Holatlar.shogirt_kasb_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data({"kasb": kasb})
    text = "🕰<b>Murojaat qilish vaqti:</b>\n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00"
    await message.answer(text=text)

    await Holatlar.shogirt_vaqt_holati.set()


@dp.message_handler(state=Holatlar.shogirt_vaqt_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    vaqt = message.text
    await state.update_data({"vaqt": vaqt})
    text = "🔎<b>Maqsad:</b>\n\nMaqsadingizni qisqacha yozib bering."
    await message.answer(text=text)
    await Holatlar.shogirt_maqsad_holati.set()

@dp.message_handler(state=Holatlar.shogirt_maqsad_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    maqsad = message.text
    await state.update_data({'maqsad':maqsad})

    malumotlar = await state.get_data()
    
    ism = malumotlar.get('ism')
    yosh = malumotlar.get('yosh')
    texnalogiya = malumotlar.get('texnalogiya')
    aloqa = malumotlar.get('aloqa')
    hudud = malumotlar.get('hudud')
    narx = malumotlar.get('narx')
    kasb = malumotlar.get('kasb')
    vaqt = malumotlar.get('vaqt')
    tg_username = message.from_user.username
    maqsad = malumotlar.get('maqsad')
    status = "Shogirt"

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=jonatish(status,ism,texnalogiya, tg_username, aloqa, hudud, narx, kasb, vaqt, maqsad, yosh))
    await message.answer(text="Barcha ma'lumotlar to'g'rimi, adminga jo'natish kerakmi?", reply_markup=tasdiqlash_buttons)
    await Holatlar.shogirt_tasdiqlash_holati.set()

@dp.message_handler(state=Holatlar.shogirt_tasdiqlash_holati, text='Ha')
async def univ(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    malumotlar = await state.get_data()

    ism = malumotlar.get('ism')
    yosh = malumotlar.get('yosh')
    texnalogiya = malumotlar.get('texnalogiya')
    aloqa = malumotlar.get('aloqa')
    hudud = malumotlar.get('hudud')
    narx = malumotlar.get('narx')
    kasb = malumotlar.get('kasb')
    vaqt = malumotlar.get('vaqt')
    tg_username = message.from_user.username
    maqsad = malumotlar.get('maqsad')
    status = "Shogirt"

    for kanal in kanallar:
        await bot.send_message(chat_id=kanal, text=jonatish(status, ism,texnalogiya, tg_username, aloqa, hudud, narx, kasb, vaqt, maqsad, yosh))
    await bot.send_message(chat_id=user_id,text="<b>✔Muaffaqiyatli jo'natildi!</b>", reply_markup=start_buttons)
    await state.finish()


@dp.message_handler(text="Yo'q", state=Holatlar.shogirt_tasdiqlash_holati)
async def univ(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id ,text="<b>Bekor qilindi</b>", reply_markup=start_buttons)
    await state.finish()





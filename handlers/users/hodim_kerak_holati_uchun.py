from aiogram import types
from states.holatlar import Holatlar
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import tasdiqlash_buttons,start_buttons
from .foydali_funksiyalar import (
    jonatish,
    )
from data.config import kanallar

from loader import dp,bot

@dp.message_handler(text='Hodim kerak')
async def bot_echo(message: types.Message):
    text = """<b>Hodim topish uchun ariza berish</b> \n\n Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering.
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
    await message.answer(text=text)
    await message.answer(text='<b>🎓 Idora nomi?</b>')
    await Holatlar.hodim_idora_holati.set()

@dp.message_handler(state=Holatlar.hodim_idora_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    idora = message.text
    await state.update_data({"idora": idora})
    text = "📚<b>Texnalogiya:</b>\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\n <i>Java, C++, C#</i>"
    await message.answer(text=text)
    await Holatlar.hodim_texnalogiya_holati.set()

@dp.message_handler(state=Holatlar.hodim_texnalogiya_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    texnalogiya = message.text
    await state.update_data({"texnalogiya": texnalogiya})
    text = "📞<b>Aloqa:</b>\n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67"
    await message.answer(text=text)
    await Holatlar.hodim_aloqa_holati.set()


@dp.message_handler(state=Holatlar.hodim_aloqa_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    aloqa = message.text
    await state.update_data({"aloqa": aloqa})
    text = "🌐<b>Hudud:</b>\n\nQaysi hududdansiz? \nViloyat nomi, Toshkent shahar yoki Respublikani kiriting."
    await message.answer(text=text)
    await Holatlar.hodim_hudud_holati.set()


@dp.message_handler(state=Holatlar.hodim_hudud_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    hudud = message.text
    await state.update_data({"hudud": hudud})
    text = "💰 Maoshni kiriting?"
    await message.answer(text=text)
    await Holatlar.hodim_narx_holati.set()

@dp.message_handler(state=Holatlar.hodim_narx_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    narx = message.text
    await state.update_data({"narx": narx})
    text = "✍️Mas'ul ism sharifi?"
    await message.answer(text=text)

    await Holatlar.hodim_masul_holati.set()

@dp.message_handler(state=Holatlar.hodim_masul_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    masul = message.text
    await state.update_data({"masul": masul})
    text = "🕰<b>Murojaat qilish vaqti:</b>\n\nQaysi vaqtda murojaat qilish mumkin? \nMasalan, 9:00 - 18:00"
    await message.answer(text=text)

    await Holatlar.hodim_mvaqt_holati.set()


@dp.message_handler(state=Holatlar.hodim_mvaqt_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    mvaqt = message.text
    await state.update_data({"mvaqt": mvaqt})
    text = "🕰 Ish vaqtini kiriting?"
    await message.answer(text=text)
    await Holatlar.hodim_vaqt_holati.set()

@dp.message_handler(state=Holatlar.hodim_vaqt_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    vaqt = message.text
    await state.update_data({"vaqt": vaqt})
    text = "‼️ Qo`shimcha ma`lumotlar?"
    await message.answer(text=text)
    await Holatlar.hodim_malumot_holati.set()

@dp.message_handler(state=Holatlar.hodim_malumot_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    mal = message.text
    await state.update_data({'mal':mal})

    malumotlar = await state.get_data()
    
    idora = malumotlar.get('idora')
    texnalogiya = malumotlar.get('texnalogiya')
    aloqa = malumotlar.get('aloqa')
    hudud = malumotlar.get('hudud')
    narx = malumotlar.get('narx')
    mvaqt = malumotlar.get('mvaqt')
    vaqt = malumotlar.get('vaqt')
    tg_username = message.from_user.username
    mal = malumotlar.get('mal')
    status = "Hodim"

    jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"🏅 Idora: <b>{idora}</b>\n" \
            f"📚 Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"📞 Aloqa: {aloqa}\n" \
            f"🌐 Hudud: {hudud}\n" \
            f"💰 Narxi: {narx}\n" \
            f"👨🏻‍💻 Ish vaqti: {vaqt}\n" \
            f"🕰 Murojaat qilish vaqti: {mvaqt}\n" \
            f"🇺🇿 Telegram: @{tg_username}\n" \
            f"🔎 Qo'shimcha ma'lumot: {mal} \n\n" \
            f"#ishJoyi #{hudud.strip()}" \

    
    texnalogiyalar = texnalogiya.split(',')
    for t in list(texnalogiyalar):
        jonatish += f' #{t.strip().lower()}'

    jonatish += f"\n\nyozuvchi: @Asadbek_Muxtorov"

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=jonatish)
    await message.answer(text="Barcha ma'lumotlar to'g'rimi, adminga jo'natish kerakmi?", reply_markup=tasdiqlash_buttons)
    await Holatlar.hodim_tasdiqlash_holati.set()

@dp.message_handler(state=Holatlar.hodim_tasdiqlash_holati, text='Ha')
async def univ(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    malumotlar = await state.get_data()
    idora = malumotlar.get('idora')
    texnalogiya = malumotlar.get('texnalogiya')
    aloqa = malumotlar.get('aloqa')
    hudud = malumotlar.get('hudud')
    narx = malumotlar.get('narx')
    mvaqt = malumotlar.get('mvaqt')
    vaqt = malumotlar.get('vaqt')
    tg_username = message.from_user.username
    mal = malumotlar.get('mal')
    status = "Hodim"

    jonatish = f"<b>{status} kerak:</b>\n\n" \
            f"🏅 Idora: <b>{idora}</b>\n" \
            f"📚 Texnalogiya: <b>{texnalogiya}</b>\n" \
            f"📞 Aloqa: {aloqa}\n" \
            f"🌐 Hudud: {hudud}\n" \
            f"💰 Narxi: {narx}\n" \
            f"👨🏻‍💻 Ish vaqti: {vaqt}\n" \
            f"🕰 Murojaat qilish vaqti: {mvaqt}\n" \
            f"🇺🇿 Telegram: @{tg_username}\n" \
            f"🔎 Qo'shimcha ma'lumot: {mal} \n\n" \
            f"#ishJoyi #{hudud.strip()}" \

    
    texnalogiyalar = texnalogiya.split(',')
    for t in list(texnalogiyalar):
        jonatish += f' #{t.strip().lower()}'

    jonatish += f"\n\nyozuvchi: @Asadbek_Muxtorov"


    for kanal in kanallar:
        await bot.send_message(chat_id=kanal, text=jonatish)
    await bot.send_message(chat_id=user_id,text="<b>✔Muaffaqiyatli jo'natildi!</b>", reply_markup=start_buttons)
    await state.finish()


@dp.message_handler(text="Yo'q", state=Holatlar.hodim_tasdiqlash_holati)
async def univ(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id ,text="<b>Bekor qilindi</b>",  reply_markup=start_buttons)
    await state.finish()





from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sherik kerak'),
            KeyboardButton(text='Ish joyi kerak'),
        ],
        [
            KeyboardButton(text='Hodim kerak'),
            KeyboardButton(text='Ustoz kerak'),
        ],
        [
            KeyboardButton(text='Shogirt kerak'),
        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ]
    ],
    resize_keyboard=True
)
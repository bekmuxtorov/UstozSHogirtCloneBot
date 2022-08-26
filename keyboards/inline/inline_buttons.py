from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

azolik_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [ 
            InlineKeyboardButton(text='Tekshirish', callback_data='tekshirish')
        ]
    ]
)

admin_control = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Kanalga yuborish'),
        ],
        [
            InlineKeyboardButton(text='Bekor qilish'),
        ]
    ]
)
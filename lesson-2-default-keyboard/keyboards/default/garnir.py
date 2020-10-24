from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


garnir = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Макарошки"),
            KeyboardButton(text="Пюрешка")
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котлетки"),
            KeyboardButton(text="Рыбка"),
        ],
    ],
    resize_keyboard=True
)


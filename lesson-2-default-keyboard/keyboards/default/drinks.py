from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


drinks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Квас"),
            KeyboardButton(text="Пиво")
        ],
    ],
    resize_keyboard=True
)

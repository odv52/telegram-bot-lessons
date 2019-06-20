from main import bot, dp
from aiogram.types import Message, CallbackQuery
from keyboards import ListOfButtons
from config import admin_id
from filters import *


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(Button("1"))
async def btn1(message: Message):
    await message.reply("Вы нажали на кнопку 1")


@dp.message_handler(Button("2"))
async def btn1(message: Message):
    await message.reply("Вы нажали на кнопку 2")


@dp.message_handler(Button("3"))
async def btn1(message: Message):
    await message.edit_reply_markup()
    await message.reply("Вы умный человек")


@dp.callback_query_handler(Button("1"))
async def btn1(call: CallbackQuery):
    await call.message.reply("Вы нажали на кнопку 1")


@dp.callback_query_handler(Button("2"))
async def btn1(call: CallbackQuery):
    await call.message.reply("Вы нажали на кнопку 2")


@dp.callback_query_handler(Button("3"))
async def btn1(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.reply("Вы умный человек")


@dp.callback_query_handler(Button("user", contains=True))
async def btn1(call: CallbackQuery):
    await call.message.edit_reply_markup()
    username = call.data.split("user ")[1]
    await call.message.reply(f"Ваш юзернейм: {username}")


@dp.message_handler()
async def keyboards(message: Message):
    text = "Нажми на кнопку"
    keyboard = ListOfButtons(
        text=["Кошелек", "Имя"],
        callback=[f"user {message.from_user.username}", "2"]
    ).inline_keyboard
    await message.reply(text=text, reply_markup=keyboard)
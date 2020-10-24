from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from loader import dp


# @dp.message_handler(Command("garnir"))
# async def show_menu(message: Message):
#     await message.answer("Выберите товар из меню ниже", reply_markup=garnir)


@dp.message_handler(Text(equals=["Квас"]))
async def get_food(message: Message):
    answer3 = message.text
    await message.answer(f"Вы выбрали " + answer3 + ". Ладно!\nЧтоб заказать еще нажмите "
                                                    "/menu", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Пиво"]))
async def get_food(message: Message):
    answer3 = message.text
    await message.answer(f"Вы выбрали " + answer3 + '.\nОчень хорошо!\nСпасибо\nЧтоб '
                                                    'заказать еще нажмите /menu', reply_markup=ReplyKeyboardMarkup())
    # если тут reply_markup=ReplyKeyboardMarkup() то клавиатуар не исчезает с экрана

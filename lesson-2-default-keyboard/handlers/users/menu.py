from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, garnir
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите основное блюдо из меню ниже", reply_markup=menu)


@dp.message_handler(Text(equals=["Котлетки"]))
async def get_food(message: Message):
    answer1 = message.text
    await message.answer(f"Вы выбрали " + answer1 + ". Отлично! \nТеперь выберите себе гарнир:", reply_markup=garnir)


@dp.message_handler(Text(equals=["Рыбка"]))
async def get_food(message: Message):
    answer1 = message.text
    await message.answer(f"🤢")
    await message.answer(
        f"Вы выбрали " + answer1 + ". Ну ок\nПростите!\nТеперь выберите себе гарнир:",
        reply_markup=garnir)


# @dp.message_handler(Text(equals=["Котлетки", "Рыбка"]))
# async def get_food(message: Message):
#     answer1 = message.text
#     await message.answer(f"Вы выбрали " + answer1 + ". Спасибо! \nТеперь выберите себе гарнир:", reply_markup=garnir)





from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import garnir, drinks
from loader import dp


# @dp.message_handler(Command("garnir"))
# async def show_menu(message: Message):
#     await message.answer("Выберите товар из меню ниже", reply_markup=garnir)


@dp.message_handler(Text(equals=["Макарошки"]))
async def get_food(message: Message):
    answer2 = message.text
    await message.answer(f"Вы выбрали " + answer2 + ". \nПюрешка кстати вкуснее!\nВыбирайте напиток: "
                                                    "/menu", reply_markup=drinks)


@dp.message_handler(Text(equals=["Пюрешка"]))
async def get_food(message: Message):
    answer2 = message.text
    await message.answer(f"Вы выбрали " + answer2 + ".\nОтличный выбор!\nВыбирайте напиток: ", reply_markup=drinks)




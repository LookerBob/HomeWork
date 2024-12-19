import asyncio
from keys import api
from crud_functions import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="Купить")]
    ], resize_keyboard=True
)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
in_button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
in_button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
kb2.add(in_button1)
kb2.insert(in_button2)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [KeyboardButton(text="Продукт 1", callback_data='product_buying'),
         KeyboardButton(text="Продукт 2", callback_data='product_buying'),
         KeyboardButton(text="Продукт 3", callback_data='product_buying'),
         KeyboardButton(text="Продукт 4", callback_data='product_buying')]
    ], resize_keyboard=True
)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберете опцию:', reply_markup=kb2)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for user in users:
        await message.answer(f'Название: Продукт {user[0]} | Описание: описание {user[1]} | Цена: {user[2]}')
        with open(f'foto{user[3]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f"Ваша норма калорий: {10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    initiate_db()
    users = get_all_products()
    executor.start_polling(dp, skip_updates=True)

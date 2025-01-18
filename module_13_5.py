from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = 'мой токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

btkey = ReplyKeyboardMarkup(resize_keyboard=True)
play = KeyboardButton(text = 'Рассчитать')
info = KeyboardButton(text = 'Информация')
btkey.add(info)
btkey.add(play)

class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()
	
@dp.message_handler(text='Рассчитать')
async def set_age(message):
	await message.answer('Введите свой возраст:')
	await UserState.age.set()
	
@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
	await state.update_data(age= message.text)
	print('Запущен алгоритм рассчета калорий')
	await message.answer('Введите свой рост:')
	await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
	await state.update_data(growth= message.text)
	await message.answer('Введите свой вес:')
	await UserState.weight.set()
	
@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
	await state.update_data(weight= message.text)
	data = await state.get_data()
	age = int(data['age'])
	growth = int(data['growth'])
	weight = int(data['weight'])
	calories  = 10 * weight + 6.25 * growth - 5 * age - 161
	await message.answer(f'Ваша норма калорий: {calories} ккал')
	await state.finish()
	

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Бот запущен')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = btkey)

@dp.message_handler(text='Информация')
async def info_message(message):
    print('Запрошена информация о  боте')
    await message.answer('Этот бот рассчитывает норму калорий для девушек')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

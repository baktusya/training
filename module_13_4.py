from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = 'мой токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()
	
@dp.message_handler(text='Calories')
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
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

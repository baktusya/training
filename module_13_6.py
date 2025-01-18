from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = 'мой токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

btkey = ReplyKeyboardMarkup(
	keyboard = [
		[KeyboardButton(text = 'Рассчитать'),
		KeyboardButton(text = 'Информация')
		]
	], resize_keyboard=True
)

inkey = InlineKeyboardMarkup(resize_keyboard=True)
calori = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
formulas = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
inkey.add(calori)
inkey.add(formulas)

class UserState(StatesGroup):
	age = State()
	growth = State()
	weight = State()
	
@dp.message_handler(text='Рассчитать' )
async def main_menu(message):
	await message.answer('Выберите опцию:', reply_markup = inkey)
	
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
	await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
	await call.answer()	
	
@dp.callback_query_handler(text='calories')
async def set_age(call):
	await call.message.answer('Введите свой возраст:')
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

class Vehicle:
  __COLOR_VARIANTS = ['белый', 'серый', 'черный', 'красный', 'зеленый', 'голубой', 'бордовый', 'оранжевый']

  def __init__(self, owner, __model, __engine_power, __color):
    self.owner = owner
    self.__model = __model
    self.__engine_power = __engine_power
    self.__color = __color

  
  def get_model(self):
    print(f'Модель: {self.__model}')
    return
  
  def get_horsepower(self):
    print(f'Мощность двигателя: {self.__engine_power}')
    return

  def get_color(self):
    print(f'Цвет: {self.__color}')
    return

  def print_info(self):
    self.get_model()
    self.get_horsepower()
    self.get_color()
    print(f'Владелец: {self.owner}')
    return

  def set_color(self, new_color):
    if new_color in self.__COLOR_VARIANTS:
       self.__color = new_color
    else:
      print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
   __PASSENGERS_LIMIT = 5
   
# Текущие цвета __COLOR_VARIANTS = ['белый', 'серый', 'черный', 'красный', 'зеленый', 'голубой', 'бордовый', 'оранжевый']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'голубой', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('розовый')
vehicle1.set_color('черный')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


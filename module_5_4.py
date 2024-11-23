class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors, *args, **kwargs):
        self.name = name
        self.number_of_floors = number_of_floors
        self.args = args
        self.kwargs = ()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
            return
        for i in range(new_floor):
            print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            return False
        print('Номер этажа не является целым числом')

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        print('Введённое значение не является числом')

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Солнечный', 12)
print(House.houses_history)
h2 = House('ЖК Лофт', 7)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        number_of_floors = self.number_of_floors
        i = 1
        for i in range(new_floor):
            if new_floor > number_of_floors or number_of_floors < 1:
                print('Такого этажа не существует')
                break
            else:
                i += 1
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Солнечный', 12)
h2 = House('ЖК Лофт', 7)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
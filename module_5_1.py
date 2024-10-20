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


h1 = House('ЖК Солнечный', 12)
h2 = House('ЖК Лофт', 7)
h1.go_to(4)
h2.go_to(8)

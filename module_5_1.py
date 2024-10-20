class House:
  def __init__(self, name, number_of_floors):
      self.name = name
      self.number_of_floors = number_of_floors
      self.go_to()
      
    def go_to(new_floor):
      nonlocal number_of_floors
      i = 1
      for i in range(new_floor):
        if new_floor > number_of_floors < 1:
          print('Такого этажа не существует')
        else:
          i += 1
          print(i)  

            
h1 = House('ЖК Солнечный', 12)
h2 = House('ЖК Лофт', 7)
h1.go_to(4)
h2.go_to(8)

import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = []
        if self.__is_valid_color(*color):
            self.__color = list(color)
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return False
        elif 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides[0] / (2 * math.pi)  # l = 2 pi r

    def get_square(self):
        return math.pi * self.__radius**2

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = list(new_sides)
            self.__radius = new_sides[0] / (2 * math.pi)
        else:
            super().set_sides(*new_sides)

    def __len__(self):
        return self.__sides[0]

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides] * self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = [new_sides[0]] * self.sides_count
        else:
            super().set_sides(*new_sides)

    def get_volume(self):
        side = self.__sides[0]
        return side**3

circle1 = Circle((200, 200, 100), (10,)) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

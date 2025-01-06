from itertools import product

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.__file = open(self.__file_name, 'a+')

    def get_products(self):
        self.__file.seek(0)
        return self.__file.read()

    def add(self, *products):
        existing_products = {}
        file_info = self.get_products().splitlines()
        for line in file_info:
            if line.strip():
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    name, weight, category = line.strip().split(', ')
                    weight = float(weight)
                    existing_products[(name, category)] = weight

        for product in products:
            prod = (product.name, product.category)
            if prod in existing_products:
                existing_products[prod] += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_products[prod]}')
            else:
                existing_products[prod] = product.weight
                print(product)

        for (name, category), weight in existing_products.items():
            self.__file.write(f'{name}, {weight}, {category}\n')

    def __del__(self):
        print('Пока')
        self.__file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
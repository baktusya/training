import threading
from time import sleep

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.days = 0

    def run(self):
        enemies = 100
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            self.days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {enemies} воинов.")
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

        return


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
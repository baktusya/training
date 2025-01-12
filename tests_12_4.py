from rt_with_exceptions import Runner
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode='w', encoding="utf-8",
                    format="%(name)s | %(levelname)s | %(asctime)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nick = Runner(name="Ник", speed=3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk_right(self):
        try:
            right_walker = Runner(name="Форест Гамп", speed=4)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            walker = Runner(name="Олег", speed= -6)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(name=548, speed=8)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


def custom_repr(self):
    return self.name

Runner.__repr__ = custom_repr


if __name__ == "__main__":
    unittest.main()



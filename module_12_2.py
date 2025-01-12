from runner_and_tournament import Runner, Tournament
import unittest


def custom_repr(self):
    return self.name

Runner.__repr__ = custom_repr

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nick = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_sprint_one(self):
        running = Tournament(90, self.usain, self.nick)
        result_one = running.start()
        self.__class__.all_results['sprint_one'] = result_one
        self.assertTrue(result_one[max(result_one.keys())] == "Ник")

    def test_sprint_two(self):
        running = Tournament(90, self.andrey, self.nick)
        result_two = running.start()
        self.__class__.all_results['sprint_two'] = result_two
        self.assertTrue(result_two[max(result_two.keys())] == "Ник")

    def test_sprint_three(self):
        running = Tournament(90, self.usain, self.andrey, self.nick)
        result_three = running.start()
        self.__class__.all_results['sprint_three'] = result_three
        self.assertTrue(result_three[max(result_three.keys())] == "Ник")

    '''проверка логики метода start с различными дистанциями, проверяем на равенство, 
    что места и имена участников соответствуют ожидаемым результатам в словаре all_results'''
    def test_sprint_four(self):
        running = Tournament(90, self.usain, self.andrey, self.nick)
        result_four = running.start()
        self.__class__.all_results['sprint_four'] = result_four
        self.assertEqual(result_four,  {1: "Усэйн", 2: "Андрей", 3: "Ник"})
        self.assertEqual(result_four[1].name, "Усэйн")
        self.assertEqual(result_four[2].name, "Андрей")
        self.assertEqual(result_four[3].name, "Ник")

    def test_sprint_five(self):
        running = Tournament(180, self.usain, self.andrey, self.nick)
        result_five = running.start()
        self.__class__.all_results['sprint_five'] = result_five
        self.assertEqual(result_five,  {1: "Усэйн", 2: "Андрей", 3: "Ник"})
        self.assertEqual(result_five[1].name, "Усэйн")
        self.assertEqual(result_five[2].name, "Андрей")
        self.assertEqual(result_five[3].name, "Ник")

if __name__ == "__main__":
    unittest.main()

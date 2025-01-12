from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner(name="Прогульщик")

        for _ in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner(name="Бегун")

        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance,100)

    def test_challenge(self):
        chellenge_walker = Runner(name="Пешеходник")
        chellenge_runner = Runner(name="Торопыга")

        for _ in range(10):
            chellenge_walker.walk()

        for _ in range(10):
            chellenge_runner.run()

        self.assertNotEqual(chellenge_walker.distance, chellenge_runner.distance)

if __name__ == "__main__":
    unittest.main()
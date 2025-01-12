from runner_and_tournament import Runner, Tournament
import unittest
import tests_12_3


first_suite = unittest.TestSuite()
first_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
first_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(first_suite)
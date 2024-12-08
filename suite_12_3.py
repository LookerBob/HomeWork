import unittest
import tests_12_3

new_test = unittest.TestSuite()
new_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
new_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

tester = unittest.TextTestRunner(verbosity=2)
tester.run(new_test)
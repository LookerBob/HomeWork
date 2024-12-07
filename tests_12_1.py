import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        x = runner.Runner("Max")
        for _ in range(10):
            x.walk()
        self.assertEqual(x.distance, 50)
    def test_run(self):
        x = runner.Runner("Max")
        for _ in range(10):
            x.run()
        self.assertEqual(x.distance, 100)
    def test_challenge(self):
        x = runner.Runner("Max")
        y = runner.Runner("Bob")
        for _ in range(10):
            x.run()
            y.walk()
        self.assertNotEqual(x.distance, y.distance)

if __name__ == "__main__":
    unittest.main()
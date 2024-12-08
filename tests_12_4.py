import rt_with_exceptions as runner
import unittest
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            x = runner.Runner("Max", -5)
            for _ in range(10):
                x.walk()
            self.assertEqual(x.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner. {err.args}', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            x = runner.Runner(12345, 300)
            for _ in range(10):
                x.run()
            self.assertEqual(x.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner. {err.args}', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            x = runner.Runner(7, 15)
            y = runner.Runner("Bob", -4)
            for _ in range(10):
                x.run()
                y.walk()
            self.assertNotEqual(x.distance, y.distance)
            logging.info('"test_challenge" выполнен успешно')
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner. {err.args}', exc_info=True)
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner. {err.args}', exc_info=True)

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                    format="%(levelname)s | %(message)s", force=True)

if __name__ == "__main__":
    unittest.main()

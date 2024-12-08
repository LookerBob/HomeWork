import runner_and_tournament as rt
import unittest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.a = rt.Runner("Усэйн",10)
        self.b = rt.Runner("Андрей", 9)
        self.c  = rt.Runner("Ник", 3)

    def test_tour_1(self):
        test = rt.Tournament(90, self.a, self.c)
        self.all_results = test.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник", "Ошибочка")
        TournamentTest.all_results[0] = self.all_results

    def test_tour_2(self):
        test = rt.Tournament(90, self.b, self.c)
        self.all_results = test.start()
        TournamentTest.all_results[1] = self.all_results
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник", "Ошибочка")

    def test_tour_3(self):
        test = rt.Tournament(90, self.a, self.b, self.c)
        self.all_results = test.start()
        TournamentTest.all_results[2] = self.all_results
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник", "Ошибочка")

    def test_tour_4(self):
        test = rt.Tournament(2, self.a, self.b, self.c)
        self.all_results = test.start()
        TournamentTest.all_results[3] = self.all_results
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник", "Ошибочка")

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            result_names = {}
            for place, runner in result.items():
                result_names[place] = runner.name
            print(result_names)
if __name__ == "__main__":
    unittest.main()

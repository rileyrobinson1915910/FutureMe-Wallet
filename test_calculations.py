import unittest
from calculations import calculate_future, core_calculations, health_score
from messages import health_score_basic, score_system, financial_health_score_full


class Testcalculations(unittest.TestCase):
    def test_calculate_future(self):
        result = calculate_future(20)
        self.assertEqual(result, (25, 30))

    def test_core_calculations(self):
        result = core_calculations(200, 100, 100)
        self.assertEqual(result, (10400, 5200, 5200))

    def test_health_score(self):
        result = health_score(10400, 5200, 5200)
        self.assertEqual(result, (0.5, 0.5))


class Testmessages(unittest.TestCase):
    def test_health_score_basic_good(self):
        result = health_score_basic(50, 100)
        self.assertEqual(result, ("Good job managing your spending!", True))

    def test_health_score_basic_bad(self):
        result = health_score_basic(100, 100)
        self.assertEqual(result, ("We need to work on your finance skills.", False))

    def test_score_system_excellent(self):
        result = score_system(0.25, 50, 100)
        self.assertEqual(result, "Excellent, your future self is on track to financial freedom!")

    def test_score_system_spending_too_high(self):
        result = score_system(0.25, 150, 100)
        self.assertEqual(result, "We need to work on controlling your spending.")

    def test_financial_health_score_full_excellent(self):
        category, message = financial_health_score_full(0.25, 0.4, 50, 100)
        self.assertEqual(category, "Excellent")
        self.assertEqual(message, "Your future self is on track to financial freedom!")

    def test_financial_health_score_full_bad(self):
        category, message = financial_health_score_full(0.05, 0.9, 150, 100)
        self.assertEqual(category, "Bad")
        self.assertEqual(message, "We need to work on controlling your spending.")


if __name__ == "__main__":
    unittest.main()

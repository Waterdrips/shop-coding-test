import unittest

from formating import format_currency


class TestFormatting(unittest.TestCase):
    def test_formatting_less_than_100(self):
        self.assertEqual("30p", format_currency(30))

    def test_formatting_more_than_100(self):
        self.assertEqual("£12.40", format_currency(1240))

    def test_formatting_exactly_100(self):
        self.assertEqual("£1.00", format_currency(100))

    def test_formatting_multiple_of_100(self):
        self.assertEqual("£1000.00", format_currency(100000))

    def test_formatting_zero(self):
        self.assertEqual("0p", format_currency(0))


if __name__ == "__main__":
    unittest.main()

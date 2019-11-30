import unittest

from goods.apples import Apples
from goods.bread import Bread
from goods.milk import Milk
from goods.soup import Soup
from offers.soup_offer import SoupOffer


class TestSoupOffer(unittest.TestCase):
    def setUp(self) -> None:
        self.soup_offer = SoupOffer(
            "Soup offer, 50% off a loaf of bread when you buy 2 soup"
        )

    def test_no_soup(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Milk()]

        text, discount = self.soup_offer.calculate_discount(basket)

        self.assertEqual(0, discount)
        self.assertEqual(None, text)

    def test_soup_no_bread(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Milk(), Soup(), Soup()]

        text, discount = self.soup_offer.calculate_discount(basket)

        self.assertEqual(0, discount)
        self.assertEqual(None, text)

    def test_only_1_soup_no_discount(self):
        basket = [
            Apples(),
            Apples(),
            Apples(),
            Apples(),
            Milk(),
            Soup(),
            Bread(),
            Bread(),
        ]

        text, discount = self.soup_offer.calculate_discount(basket)

        self.assertEqual(0, discount)
        self.assertEqual(None, text)

    def test_odd_number_of_soup_more_bread(self):
        basket = [
            Soup(),
            Soup(),
            Soup(),
            Soup(),
            Soup(),
            Bread(),
            Bread(),
            Bread(),
            Bread(),
        ]

        text, discount = self.soup_offer.calculate_discount(basket)
        expected = int(Bread().pence_price / 2).__floor__() * 2

        self.assertEqual(expected, discount)
        self.assertEqual(
            f"Soup, Buy 2 and get 50% off a loaf of Bread: -{expected}p", text
        )

    def test_no_soup_lots_bread(self):
        basket = [Bread(), Bread(), Bread(), Bread()]

        text, discount = self.soup_offer.calculate_discount(basket)

        self.assertEqual(0, discount)
        self.assertEqual(None, text)

    def test_more_bread_than_discount(self):
        basket = [Apples(), Milk(), Soup(), Soup(), Bread(), Bread()]

        text, discount = self.soup_offer.calculate_discount(basket)

        expected = int(Bread().pence_price / 2).__floor__()

        self.assertEqual(expected, discount)
        self.assertEqual(
            f"Soup, Buy 2 and get 50% off a loaf of Bread: -{expected}p", text
        )

    def test_less_bread_than_discount(self):
        basket = [Soup(), Soup(), Soup(), Soup(), Bread()]

        text, discount = self.soup_offer.calculate_discount(basket)

        expected = int(Bread().pence_price / 2).__floor__()

        self.assertEqual(expected, discount)
        self.assertEqual(
            f"Soup, Buy 2 and get 50% off a loaf of Bread: -{expected}p", text
        )

    def test_no_items(self):
        basket = []

        text, discount = self.soup_offer.calculate_discount(basket)

        self.assertEqual(0, discount)
        self.assertEqual(None, text)


if __name__ == "__main__":
    unittest.main()

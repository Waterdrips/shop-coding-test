import unittest

from goods.apples import Apples
from goods.bread import Bread
from goods.soup import Soup
from offers.apple_offer import AppleOffer


class TestAppleOffer(unittest.TestCase):
    def test_apply_single_apple(self):
        basket = [Apples()]
        text, discount = AppleOffer.apply(basket)

        discount_per_apple = int(Apples.pence_price / 10).__ceil__()

        self.assertEqual(discount_per_apple, discount)
        self.assertEqual("Apples 10% off: -10p", text)

    def test_apply_many_apples(self):
        basket = [Apples(), Apples(), Apples(), Apples()]
        text, discount = AppleOffer.apply(basket)

        discount_per_apple = int(Apples.pence_price / 10).__ceil__()

        self.assertEqual(basket.count(Apples()) * discount_per_apple, discount)
        self.assertEqual("Apples 10% off: -40p", text)

    def test_apply_apples_and_other_items(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Bread(), Soup()]
        text, discount = AppleOffer.apply(basket)

        discount_per_apple = int(Apples.pence_price / 10).__ceil__()

        self.assertEqual(basket.count(Apples()) * discount_per_apple, discount)
        self.assertEqual("Apples 10% off: -40p", text)

    def test_apply_no_apples_other_items(self):
        basket = [Bread(), Soup()]
        text, discount = AppleOffer.apply(basket)

        discount_per_apple = int(Apples.pence_price / 10).__ceil__()

        self.assertEqual(basket.count(Apples()) * discount_per_apple, discount)
        self.assertEqual(None, text)

    def test_apply_no_items(self):
        basket = []
        text, discount = AppleOffer.apply(basket)

        discount_per_apple = int(Apples.pence_price / 10).__ceil__()

        self.assertEqual(basket.count(Apples()) * discount_per_apple, discount)
        self.assertEqual(None, text)

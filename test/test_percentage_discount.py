import unittest
from typing import *

from goods.apples import Apples
from goods.bread import Bread
from goods.shop_item import ShopItem
from goods.soup import Soup
from offers.percentage_offer import PercentageOffer


class TestPercentageOffer(unittest.TestCase):
    @staticmethod
    def count_items_of_type(basket: List[ShopItem], item_type: type) -> int:
        return sum(isinstance(item, item_type) for item in basket)

    @staticmethod
    def discount_each(price: int, percentage: float) -> int:
        return int(price * (percentage / 100)).__floor__()

    def test_apply_single_apple(self):
        percentage = 10
        offer = PercentageOffer("Apple discount", Apples, percentage)
        basket = [Apples()]
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = int(Apples().pence_price / percentage).__floor__()

        self.assertEqual(discount_per_apple, discount)
        self.assertEqual("Apples 10% off: -10p", text)

    def test_apply_many_apples(self):
        basket = [Apples(), Apples(), Apples(), Apples()]
        percentage = 10.11
        offer = PercentageOffer("Apple discount", Apples, percentage)
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = self.discount_each(Apples().pence_price, percentage)

        self.assertEqual(
            self.count_items_of_type(basket, Apples) * discount_per_apple, discount
        )
        self.assertEqual("Apples 10.11% off: -40p", text)

    def test_apply_apples_and_other_items(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Bread(), Soup()]
        percentage = 25
        offer = PercentageOffer("Apple discount", Apples, percentage)
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = int(Apples().pence_price * (percentage / 100)).__floor__()

        self.assertEqual(
            self.count_items_of_type(basket, Apples) * discount_per_apple, discount
        )
        self.assertEqual(f"Apples {percentage}% off: -£1.00", text)

    def test_apply_no_apples_other_items(self):
        basket = [Bread(), Soup()]
        percentage = 25
        offer = PercentageOffer("Apple discount", Apples, percentage)
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = self.discount_each(Apples().pence_price, percentage)

        self.assertEqual(basket.count(Apples) * discount_per_apple, discount)
        self.assertEqual(None, text)

    def test_apply_no_items(self):
        basket = []
        percentage = 10
        offer = PercentageOffer("Apple discount", Apples, percentage)
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = int(Apples().pence_price / percentage).__ceil__()

        self.assertEqual(basket.count(Apples()) * discount_per_apple, discount)
        self.assertEqual(None, text)

    def test_apply_more_items_in_basket_than_discount(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Bread(), Soup()]
        percentage = 25
        number_on_offer = 2
        offer = PercentageOffer("Apple discount", Apples, percentage, number_on_offer)
        text, discount = offer.calculate_discount(basket)

        discount_per_apple = int(Apples().pence_price * (percentage / 100)).__floor__()

        self.assertEqual(discount_per_apple * number_on_offer, discount)
        self.assertEqual(f"Apples {percentage}% off: -50p", text)

    def test_apply_less_items_basked_than_discount(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Bread(), Soup()]
        percentage = 25
        number_on_offer = 2
        offer = PercentageOffer("Apple discount", Apples, percentage, number_on_offer)

        text, discount = offer.calculate_discount(basket)

        discount_per_apple = int(Apples().pence_price * (percentage / 100)).__floor__()

        self.assertEqual(2 * discount_per_apple, discount)
        self.assertEqual(f"Apples {percentage}% off: -50p", text)

    def test_apply_no_quantity_of_discount(self):
        basket = [Apples(), Apples(), Apples(), Apples(), Bread(), Soup()]
        percentage = 25
        number_on_offer = 0
        offer = PercentageOffer("Apple discount", Apples, percentage, number_on_offer)
        text, discount = offer.calculate_discount(basket)
        self.assertEqual(0, discount)
        self.assertEqual(None, text)

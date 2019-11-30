import unittest

from basket.basket import Basket
from goods.apples import Apples
from goods.bread import Bread
from goods.milk import Milk
from goods.soup import Soup
from offers.percentage_offer import PercentageOffer
from offers.soup_offer import SoupOffer


class TestCreateBasketFromList(unittest.TestCase):
    def setUp(self) -> None:
        self.products = {"apples": Apples, "bread": Bread, "soup": Soup, "milk": Milk}

        self.offers = [
            PercentageOffer("Apples, 10% off", Apples, 10),
            SoupOffer("Buy 2 soup and get 50% off a loaf of bread"),
        ]

    def test_empty_list(self):
        items = []
        basket = Basket(items, self.offers, self.products)
        self.assertEqual([], basket.found_goods)

    def test_single_item(self):
        items = ["Apples"]

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(1, len(basket.found_goods))

    def test_lots_items(self):
        items = ["Apples", "Soup", "Bread", "Soup", "Milk"]

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(5, len(basket.found_goods))

    def test_some_invalid_items(self):
        items = [
            "Apples",
            "Soup",
            "Bread",
            "Soup",
            "Milk",
            "Random",
            "Stuff",
            "Bread,Milk",
        ]
        basket = Basket(items, self.offers, self.products)

        self.assertEqual(5, len(basket.found_goods))

    def test_all_invalid_items(self):
        items = ["Ap", "up", "d", "", "l"]

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(0, len(basket.found_goods))

    def test_random_case_items(self):
        items = ["bREad", "MILK", "sOup", "appleS", "soup"]
        basket = Basket(items, self.offers, self.products)
        self.assertEqual(5, len(basket.found_goods))


class TestCalculateFullPrice(unittest.TestCase):
    def setUp(self) -> None:
        self.products = {"apples": Apples, "bread": Bread, "soup": Soup, "milk": Milk}

        self.offers = []

    def test_no_items(self):
        items = []

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(0, basket.full_price)

    def test_one_item(self):
        items = ["Apples"]

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(Apples().pence_price, basket.full_price)

    def test_multiple_same_items(self):
        items = ["Apples", "apples"]

        basket = Basket(items, self.offers, self.products)
        self.assertEqual(2 * Apples().pence_price, basket.full_price)

    def test_many_items(self):
        items = ["Apples", "apples", "Bread", "Milk", "soup", "SOUP"]

        basket = Basket(items, self.offers, self.products)

        self.assertEqual(540, basket.full_price)

    def test_some_invalid_items(self):
        items = [
            "Apples",
            "apples",
            "Bread",
            "Milk",
            "soup",
            "SOUP",
            "NOT",
            "An",
            "item",
        ]

        basket = Basket(items, self.offers, self.products)

        self.assertEqual(540, basket.full_price)

    def test_all_invalid_items(self):
        items = ["NOT", "An", "item"]

        basket = Basket(items, self.offers, self.products)

        self.assertEqual(0, basket.full_price)


if __name__ == "__main__":
    unittest.main()

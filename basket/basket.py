from typing import *

from goods.shop_item import ShopItem
from offers.offer import Offer


class Basket:
    def __init__(
        self, shopping_list: List[str], offers: List[Offer], products: Dict[str, type]
    ):
        self.shopping_list = shopping_list
        self.offers = offers
        self.found_goods, self.rejected_items = self._fill_basket_from_list(
            shopping_list, products
        )
        self.full_price = sum([item.pence_price for item in self.found_goods])
        self.discount, self.discount_messages = self.calculate_discounts()
        self.total_price = self.full_price - self.discount

    @staticmethod
    def _fill_basket_from_list(
        shopping_list: list, products: Dict[str, type]
    ) -> Tuple[List[ShopItem], List[str]]:
        """
        Convert a list of items into a filled basket, filter out anything we dont sell and return that in a list
        """
        rejected_items = [
            item for item in shopping_list if item.lower() not in products.keys()
        ]
        items = [
            products.get(item.lower())()
            for item in shopping_list
            if item.lower() in products.keys()
        ]

        return items, rejected_items

    def calculate_discounts(self) -> Tuple[int, Optional[List]]:
        discount = 0
        discount_messages = []
        for offer in self.offers:
            message, this_discount = offer.calculate_discount(self.found_goods)
            discount += this_discount
            if message is not None:
                discount_messages.append(message)
        return discount, discount_messages

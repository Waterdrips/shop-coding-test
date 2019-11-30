from goods.shop_item import ShopItem
from typing import *


class Offer:
    @staticmethod
    def count_item_in_basket(basket: List[ShopItem], item_type: type) -> int:
        return sum(isinstance(item, item_type) for item in basket)

    def calculate_discount(self, basket: List[ShopItem]) -> Tuple[str, int]:
        """
        Implement the calculate_discount method in the custom discount classes
        """
        raise NotImplementedError

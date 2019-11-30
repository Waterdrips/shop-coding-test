from typing import List, Tuple

from goods.shop_item import ShopItem
from offers.offer import Offer


class AppleOffer(Offer):
    def __init__(self, name, output_text):
        super().__init__(name, output_text)

    @staticmethod
    def apply(basket: List[ShopItem]) -> Tuple[str, int]:
        message = ""
        discount = 0
        return message, discount

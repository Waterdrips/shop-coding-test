from goods.shop_item import ShopItem
from typing import *


class Offer:
    @staticmethod
    def apply(basket: List[ShopItem]) -> Tuple[str, int]:
        # Force our developers to implement this on their offer
        raise NotImplementedError

from typing import List, Tuple

from formating import format_currency
from goods.apples import Apples
from goods.shop_item import ShopItem
from offers.offer import Offer


class AppleOffer(Offer):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def apply(basket: List[ShopItem]) -> Tuple[str, int]:
        """
        apply takes a list of items, and return a discount that is 10% of the cost of each apple
        """
        quantity = basket.count(Apples())

        # if our discount is partial pence, then we round down - profit
        discount = int(Apples.pence_price / 10).__floor__() * quantity

        message = (
            f"Apples 10% off: -{format_currency(discount)}" if quantity > 0 else None
        )

        return message, discount

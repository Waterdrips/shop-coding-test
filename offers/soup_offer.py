from typing import List, Tuple

from goods.bread import Bread
from goods.shop_item import ShopItem
from goods.soup import Soup
from offers.offer import Offer
from formating import format_currency
from offers.percentage_offer import PercentageOffer


class SoupOffer(Offer):
    def __init__(self, name):
        self.name = name

    def calculate_discount(self, basket: List[ShopItem]) -> Tuple[str, int]:
        """
        Custom offer, this offer is: For every 2x soup in the basket, the shopper gets 50% off a loaf of bread
        """
        soup_quantity = self.count_item_in_basket(basket, Soup)
        bread_discount_max_quantity = int(soup_quantity / 2).__floor__()
        bread_quantity = self.count_item_in_basket(basket, Bread)

        # Get the number of bread we could apply discount on
        discount_quantity = min(bread_quantity, bread_discount_max_quantity)

        bread_offer = PercentageOffer(
            "Bread Offer if you buy Soup", Bread, 50, discount_quantity
        )
        _, discount = bread_offer.calculate_discount(basket)

        message = (
            f"Soup, Buy 2 and get 50% off a loaf of Bread: -{format_currency(discount)}"
            if discount > 0
            else None
        )
        return message, discount

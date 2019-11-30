from typing import List, Tuple, Optional

from formating import format_currency
from goods.shop_item import ShopItem
from offers.offer import Offer


class PercentageOffer(Offer):
    """
    By creating an object from this class you create a % off offer
    This will allow calculation of a discount for the basket, based on the percentage and item to apply the discount to
    These config parameters are passed in when creating the discount object

    The offer can apply to all (default) items in the passed basket, or a specified max_items
    """

    def __init__(
        self, name, discount_item_type: type, percentage: float, max_items: int = None
    ):
        self.name = name
        self.discount_item_type = discount_item_type
        self.percentage = percentage
        self.max_items = max_items

    def calculate_discount(self, basket: List[ShopItem]) -> Tuple[Optional[str], int]:
        """
        Take a list of items, and return a discount that based on specified percentage and max quantity of items
        """
        if self.max_items == 0:
            return None, 0

        quantity = self.count_item_in_basket(basket, self.discount_item_type)

        # If we have been given a max number of items to apply this to, then see if we have more than that in the bag
        if self.max_items and quantity > self.max_items:
            quantity = self.max_items

        # if our discount is partial pence, then we round down - profit
        discount_each = int(
            self.discount_item_type().pence_price * (self.percentage / 100)
        ).__floor__()

        discount_total = quantity * discount_each

        message = (
            f"{self.discount_item_type().name} {self.percentage}% off: -{format_currency(discount_total)}"
            if quantity > 0
            else None
        )

        return message, discount_total

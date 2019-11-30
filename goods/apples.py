from dataclasses import dataclass

from goods.shop_item import ShopItem


@dataclass
class Apples(ShopItem):
    """
    Apples Shop Item, it has a default price set in here, but can be overridden in other areas of the program if required
    """

    name: str = "apples"
    pence_price: int = 100

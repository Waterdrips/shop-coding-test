from dataclasses import dataclass

from goods.shop_item import ShopItem


@dataclass
class Soup(ShopItem):
    """
    Soup Shop Item, it has a default price set in here, but can be overridden in other areas of the program if required
    """

    name: str = "soup"
    pence_price: int = 65

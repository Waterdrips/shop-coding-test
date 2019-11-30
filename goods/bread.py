from dataclasses import dataclass

from goods.shop_item import ShopItem


@dataclass
class Bread(ShopItem):
    """
    Bread Shop Item, it has a default price set in here, but can be overridden in other areas of the program if required
    """

    name: str = "bread"
    pence_price: int = 80

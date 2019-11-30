from goods.shop_item import ShopItem


class Bread(ShopItem):
    """
    Bread Shop Item, it has a default price set in here, but can be overridden in other areas of the program if required
    """

    def __init__(self):
        super().__init__("Bread", 80)

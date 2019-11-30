from goods.shop_item import ShopItem


class Bread(ShopItem):
    def __init__(self):
        super().__init__("Bread", 80)

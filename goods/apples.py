from goods.shop_item import ShopItem


class Apples(ShopItem):
    def __init__(self):
        super().__init__("Apples", 100)

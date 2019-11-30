from goods.apples import Apples
from offers.percentage_offer import PercentageOffer
from offers.soup_offer import SoupOffer

# This week's offers
offers = [
    PercentageOffer("Apples, 10% off", Apples, 10),
    SoupOffer("Buy 2 soup and get 50% off a loaf of bread"),
]

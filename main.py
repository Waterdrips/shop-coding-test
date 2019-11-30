import logging
import sys

from basket.basket import Basket
from formating import format_currency
from store import current_offers
from store import products

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# These are pulled in from the "store" directory. they can be amended in there, we dont need to know about the details
offers = current_offers.offers
current_products = products.products


def main(input_items: list) -> None:
    """
    Program entry point, we have already grabbed all of the inputs and passed them into this function
    """
    basket = Basket(input_items, offers, current_products)

    print(f"Subtotal: {format_currency(basket.full_price)}")

    if len(basket.discount_messages) == 0:
        print("(no offers available)")
    else:
        for msg in basket.discount_messages:
            print(msg)
    print(f"Total: {format_currency(basket.total_price)}")


if __name__ == "__main__":
    # first element is the called filename - so we exclude it,
    inputs = sys.argv[1:]
    main(inputs)

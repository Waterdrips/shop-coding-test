import logging
import sys

from goods.apples import Apples
from goods.bread import Bread
from goods.milk import Milk
from goods.soup import Soup

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

products = {"apples": Apples, "bread": Bread, "soup": Soup, "milk": Milk}


def fill_basket_from_list(input_items: list) -> list:
    """
    Convert a list of items into a filled basket, filter out anything we dont sell
    """
    rejected_items = [item for item in inputs if item not in products.keys()]
    logger.debug(rejected_items)

    return [products.get(item)() for item in input_items if item in products.keys()]


def main(input_items: list) -> None:
    """
    Program entry point, we have already grabbed all of the inputs and passed them into this function
    """
    basket = fill_basket_from_list(input_items)

    # TODO run through the list of available offers, keep a count of the total discount, then grab the list price, do the diff and format the output

    logger.info(basket)


if __name__ == "__main__":
    # first element is the called filename - so we exclude it,
    inputs = sys.argv[1:]

    if "--debug" in inputs:
        logger.setLevel(logging.DEBUG)
        logger.debug("Set log level to debug")
        inputs.remove("--debug")

    main(inputs)

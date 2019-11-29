import logging
import sys

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main(inputs: list) -> None:
    """
    Program entry point, we have already grabbed all of the inputs and passed them into this function
    """
    pass


if __name__ == "__main__":
    # first element is the called filename - so we exclude it,
    # the rest could be space separated, or comma/space if we get malformed user input
    # we can deal with that though
    inputs = sys.argv[1:]

    main(inputs)

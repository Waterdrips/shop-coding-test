def format_currency(amount: int) -> str:
    """
    format_currenct takes an int, and returns it with "p" on the end if < 100, or converts it to £x.xx if above 99
    """

    if amount < 100:
        # display pence
        return f"{amount}p"

    # divide by 100, return the number of pounds
    # after the decimal point we format to 2 digits, so 0 --> 00
    return f"£{int(amount/100).__floor__()}.{amount % 100:02d}"

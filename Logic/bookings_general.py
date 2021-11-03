from Domain.booking import *


def bookings_general_sort_decreasingly_by_price(bookings: list[dict]) -> list[dict]:
    """
    Sorts the given list of bookings in decreasing order, by price.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings to sort.

    Returns
    -------
    list[dict]:
        A new list containing the bookings from the given list, but sorted decreasingly, by price.
    """
    sorted_list = sorted(bookings, key=booking_get_price, reverse=True)
    return sorted_list


def bookings_general_find_maximum_price_for_class_type(bookings: list[dict], class_type: str) -> float:
    """
    Given a class type (Economy, Economy Plus or Business), find the maximum price among the bookings having
    this class type.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings
    class_type : str
        The class type.

    Returns
    -------
    float or None:
        The maximum price among bookings having the given class type, None if such bookings do not exist.
    """

    # make a list of all the prices for the bookings of the given class type
    prices = []
    for booking in bookings:
        if booking_get_class_type(booking) == class_type:
            prices.append(booking_get_price(booking))

    if len(prices) == 0:
        return None

    # "HACK".. no time :(
    return sorted(prices)[-1]

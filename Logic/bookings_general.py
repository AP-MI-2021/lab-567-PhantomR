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
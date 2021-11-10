from typing import Optional

from Domain.booking import *
from Logic.booking_crud import crud_get_bookings_for_name
from Logic.bookings_manager import bookings_manager_record_modification, bookings_manager_get_current_list, \
    bookings_manager_set_current_list


def bookings_general_sort_decreasingly_by_price(bookings_manager: dict):
    """
    Sorts the given list of bookings in decreasing order, by price.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager we operate on.

    Returns
    -------
    list[dict]:
        A new list containing the bookings from the given list, but sorted decreasingly, by price.
    """
    bookings_manager_record_modification(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    sorted_bookings = sorted(bookings, key=booking_get_price, reverse=True)
    bookings_manager_set_current_list(bookings_manager, sorted_bookings)


def bookings_general_find_maximum_price_for_class_type(bookings: list[dict], class_type: str) -> Optional[float]:
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


def bookings_general_compute_total_price_of_reservations_for_name(bookings_manager: dict, name: str) -> float:
    """
    Given a Bookings Manager and a name, compute the total price of all bookings under the given name.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager.
    name : str
        The name in the bookings we are computing the total price for.

    Returns
    -------
    float :
        The total price of the bookings under the given name or -1, if the name does not exist.

    """
    bookings_for_name = crud_get_bookings_for_name(bookings_manager, name)

    price_total = -1
    for booking in bookings_for_name:
        booking_price = booking_get_price(booking)

        if price_total == -1:
            price_total = 0
        price_total += booking_price

    return price_total


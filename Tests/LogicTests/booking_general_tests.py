from Logic.bookings_general import *
from Logic.booking_crud import *


def is_sorted_decreasingly_by_price(bookings: list[dict]) -> bool:
    """
    Tests whether the given list of Bookings is sorted decreasingly by price.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings to check.

    Returns
    -------
    bool:
        True, if the list is sorted decreasingly by price. False, otherwise.

    """
    for i in range(len(bookings) - 1):
        price_of_i_th_booking = booking_get_price(bookings[i])
        price_of_i_plus_1_th_booking = booking_get_price(bookings[i+1])
        if price_of_i_th_booking < price_of_i_plus_1_th_booking:
            return False

    return True


def test_bookings_general_sort_decreasingly_by_price():
    # create a list of bookings to work on
    bookings = []
    bookings = crud_insert_booking(bookings, 1, "Alexandru Duna", "Economy", 100.0, True)
    bookings = crud_insert_booking(bookings, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    bookings = crud_insert_booking(bookings, 3, "Bill Tractor", "Business", 500.0, True)
    bookings = crud_insert_booking(bookings, 4, "Cosmin Piersica", "Business", 1000.0, True)
    bookings = crud_insert_booking(bookings, 5, "Sergiu Vasile Covor", "Economy", 50.0, False)

    bookings = bookings_general_sort_decreasingly_by_price(bookings)
    assert is_sorted_decreasingly_by_price(bookings)



def run_booking_general_tests():
    test_bookings_general_sort_decreasingly_by_price()
    print("[TESTS] All bookings general tests passed.")
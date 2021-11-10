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
    bookings_manager = bookings_manager_create()

    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Cosmin Piersica", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Sergiu Vasile Covor", "Economy", 50.0, False)

    bookings_general_sort_decreasingly_by_price(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert is_sorted_decreasingly_by_price(bookings)


def test_bookings_general_find_maximum_price_for_class_type():
    # create a list of bookings to work on
    bookings_manager = bookings_manager_create()
    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Cosmin Piersica", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Sergiu Vasile Covor", "Economy", 50.0, False)

    bookings = bookings_manager_get_current_list(bookings_manager)
    assert bookings_general_find_maximum_price_for_class_type(bookings, "Economy") == 100.0
    assert bookings_general_find_maximum_price_for_class_type(bookings, "Economy Plus") == 200.0
    assert bookings_general_find_maximum_price_for_class_type(bookings, "Business") == 1000.0
    assert bookings_general_find_maximum_price_for_class_type(bookings, "CLASS WITH NO BOOKINGS") is None


def test_compute_total_price_of_reservations_for_name():
    # create a list of bookings to work on
    bookings_manager = bookings_manager_create()
    crud_insert_booking(bookings_manager, 1, "Ion Pisoi", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Alexandru Duna", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Ion Pisoi", "Economy", 50.0, False)

    total_price = bookings_general_compute_total_price_of_reservations_for_name(bookings_manager, "Ion Pisoi")
    assert total_price == (100.0 + 200.0 + 50.0)

    total_price = bookings_general_compute_total_price_of_reservations_for_name(bookings_manager, "NAME NOT PRESENT")
    assert total_price == -1.0

    total_price = bookings_general_compute_total_price_of_reservations_for_name(bookings_manager, "Bill Tractor")
    assert total_price == 500.0


def test_discount_checked_in_reservations():
    # create a list of bookings to work on
    bookings_manager = bookings_manager_create()
    crud_insert_booking(bookings_manager, 1, "Ion Pisoi", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Alexandru Duna", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Ion Pisoi", "Economy", 50.0, False)

    bookings_general_discount_checked_in_reservations(bookings_manager, 50)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert booking_get_price(crud_get_booking(bookings, 1)) == 50.0
    assert booking_get_price(crud_get_booking(bookings, 3)) == 250.0
    assert booking_get_price(crud_get_booking(bookings, 4)) == 500.0
    assert booking_get_price(crud_get_booking(bookings, 2)) == 200.0
    assert booking_get_price(crud_get_booking(bookings, 5)) == 50.0


def run_booking_general_tests():
    test_bookings_general_sort_decreasingly_by_price()
    test_bookings_general_find_maximum_price_for_class_type()
    test_compute_total_price_of_reservations_for_name()
    test_discount_checked_in_reservations()
    print("[TESTS] All bookings general tests passed.")

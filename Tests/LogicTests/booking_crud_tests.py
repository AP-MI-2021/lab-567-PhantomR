from Logic.booking_crud import *


def test_booking_crud():
    bookings_manager = bookings_manager_create()
    bookings = bookings_manager_get_current_list(bookings_manager)

    # test insertion and getting booking by id
    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    assert len(bookings) == 1
    assert booking_get_id(crud_get_booking(bookings, 1)) == 1

    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    assert len(bookings) == 2
    assert booking_get_name(crud_get_booking(bookings, 2)) == "Ion Pisoi"

    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    assert len(bookings) == 3
    assert booking_get_class_type(crud_get_booking(bookings, 3)) == "Business"

    crud_insert_booking(bookings_manager, 4, "Cosmin Piersica", "Business", 1000.0, True)
    assert len(bookings) == 4
    assert booking_get_price(crud_get_booking(bookings, 4)) == 1000.0

    crud_insert_booking(bookings_manager, 5, "Sergiu Vasile Covor", "Economy", 50.0, False)
    assert len(bookings) == 5
    assert booking_get_checked_in(crud_get_booking(bookings, 5)) is False

    # test deleting two bookings successively
    crud_delete_booking(bookings_manager, 5)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 4
    crud_delete_booking(bookings_manager, 1)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 3

    # test editing a booking
    crud_edit_booking(bookings_manager, 4, "Cosmin Prunariu-Piersica", "Economy Plus", 1000.0, True)
    assert len(bookings) == 3
    # retrieve the edited booking to test the modifications
    booking = crud_get_booking(bookings, 4)
    assert booking_get_id(booking) == 4
    assert booking_get_name(booking) == "Cosmin Prunariu-Piersica"
    assert booking_get_class_type(booking) == "Economy Plus"
    assert booking_get_price(booking) == 1000.0
    assert booking_get_checked_in(booking)


def test_get_bookings_for_name():
    bookings_manager = bookings_manager_create()
    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Alexandru Duna", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Sergiu Vasile Covor", "Economy", 50.0, False)

    bookings_for_alexandru_duna = crud_get_bookings_for_name(bookings_manager, "Alexandru Duna")
    assert len(bookings_for_alexandru_duna) == 2

    bookings_for_nobody = crud_get_bookings_for_name(bookings_manager, "NOBODY")
    assert len(bookings_for_nobody) == 0

    bookings_for_ion_pisoi = crud_get_bookings_for_name(bookings_manager, "Ion Pisoi")
    assert len(bookings_for_ion_pisoi) == 1


def run_booking_crud_tests():
    test_booking_crud()
    test_get_bookings_for_name()
    print("[TESTS] All Booking CRUD tests passed.")

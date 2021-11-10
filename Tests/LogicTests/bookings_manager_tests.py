from Logic.booking_crud import *
from Logic.bookings_manager import *


def test_undo_redo():
    bookings_manager = bookings_manager_create()
    bookings = bookings_manager_get_current_list(bookings_manager)

    # INSERTION UNDO / REDO
    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    assert len(bookings) == 1
    assert booking_get_id(crud_get_booking(bookings, 1)) == 1

    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    assert len(bookings) == 2
    assert booking_get_name(crud_get_booking(bookings, 2)) == "Ion Pisoi"

    bookings_manager_apply_undo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 1

    bookings_manager_apply_undo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 0

    # redundant undo
    bookings_manager_apply_undo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 0

    bookings_manager_apply_redo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 1

    bookings_manager_apply_redo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 2

    # redundant redo
    bookings_manager_apply_redo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 2

    # DELETION UNDO / REDO
    crud_delete_booking(bookings_manager, 1)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 1

    bookings_manager_apply_undo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 2

    bookings_manager_apply_redo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    assert len(bookings) == 1

    # EDIT UNDO / REDO

    bookings = bookings_manager_get_current_list(bookings_manager)
    booking = crud_get_booking(bookings, 2)
    assert booking_get_name(booking) == "Ion Pisoi"
    crud_edit_booking(bookings_manager, 2, "Cosmin Prunariu-Piersica", "Economy Plus", 1000.0, True)
    bookings = bookings_manager_get_current_list(bookings_manager)
    booking = crud_get_booking(bookings, 2)
    assert booking_get_name(booking) == "Cosmin Prunariu-Piersica"

    bookings_manager_apply_undo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    booking = crud_get_booking(bookings, 2)
    assert booking_get_name(booking) == "Ion Pisoi"

    bookings_manager_apply_redo(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)
    booking = crud_get_booking(bookings, 2)
    assert booking_get_name(booking) == "Cosmin Prunariu-Piersica"


def run_bookings_manager_tests():
    test_undo_redo()
    print("[TESTS] All bookings manager tests passed.")

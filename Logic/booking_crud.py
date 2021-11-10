from Domain.booking import *
from Logic.bookings_manager import *


def crud_insert_booking(bookings_manager: dict, id_: int, name: str, class_type: str, price: float, checked_in: bool):
    """
    Inserts a new Booking with the given attributes in a given a Bookings Manager.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager (contains the list of bookings to modify).
    id_ : int
        The value of the id attribute of the booking to insert.
    name : str
        The value of the name attribute of the booking to insert.
    class_type : str
        The value of the class type attribute of the booking to insert.
    price : float
        The value of the price attribute of the booking to insert
    checked_in : bool
        The value of the checked in attribute of the booking to insert.
    """
    bookings_manager_record_modification(bookings_manager)

    bookings = bookings_manager_get_current_list(bookings_manager)
    new_booking = booking_create(id_, name, class_type, price, checked_in)
    bookings.append(new_booking)


def crud_delete_booking(bookings_manager: dict, id_: int):
    """
    Deleted the booking having the given id from the given list of bookings, if it exists.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager (contains the list of bookings to modify).
    id_ : int
        The id of the booking to delete.
    """
    bookings_manager_record_modification(bookings_manager)

    bookings = bookings_manager_get_current_list(bookings_manager)
    new_bookings = []
    for booking in bookings:
        if booking_get_id(booking) != id_:
            new_bookings.append(booking)

    bookings_manager_set_current_list(bookings_manager, new_bookings)


def crud_edit_booking(
        bookings_manager: dict, id_: int, new_name: str, new_class_type: str, new_price: float, new_checked_in: bool):
    """
    Edits the booking having the given id from the given list of bookings.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager (contains the list of bookings to modify).
    id_ : int
        The id of the booking to edit.
    new_name : str
        The new name of the booking to edit.
    new_class_type : str
        The new class type of the booking to edit.
    new_price : float
        The new price of the booking to edit.
    new_checked_in : bool
        The new value for the checked attribute of the booking to edit.
    """
    bookings_manager_record_modification(bookings_manager)
    bookings = bookings_manager_get_current_list(bookings_manager)

    for i in range(len(bookings)):
        if booking_get_id(bookings[i]) == id_:
            bookings[i] = booking_create(id_, new_name, new_class_type, new_price, new_checked_in)
            break


def crud_get_booking(bookings, id_):
    """
    Retrieves a booking having the given id from the given list of bookings.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings.
    id_ :
        The id of the booking to retrieve.

    Returns
    -------
    dict or None:
        A dict representing a booking if a booking with the given id_ exists, None if it does not exist.

    """
    for booking in bookings:
        if booking_get_id(booking) == id_:
            return booking
    return None

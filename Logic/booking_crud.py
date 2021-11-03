from Domain.booking import *


def crud_insert_booking(bookings: list[dict], id_: int, name: str, class_type: str, price: float, checked_in: bool):
    """
    Inserts a new Booking with the given attributes in a given list of bookings.

    Parameters
    ----------
    bookings : list[dict]
        The given list of bookings.

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

    Returns
    -------
    list[dict]:
        A new list containing copies of the previously existing bookings along with the newly created one.
    """
    new_booking = booking_create(id_, name, class_type, price, checked_in)
    new_bookings = bookings + [new_booking]

    return new_bookings


def crud_delete_booking(bookings: list[dict], id_: int):
    """
    Deleted the booking having the given id from the given list of bookings, if it exists.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings.
    id_ : int
        The id of the booking to delete.

    Returns
    -------
    list[dict]:
        A new list containing copies of the bookings in the given list, except for the one to delete, if it existed.
    """
    new_bookings = []
    for booking in bookings:
        if booking_get_id(booking) != id_:
            # we skip the booking we want to delete
            new_bookings.append(booking)

    return new_bookings


def crud_edit_booking(
        bookings: list[dict], id_: int, new_name: str, new_class_type: str, new_price: float, new_checked_in: bool):
    """
    Edits the booking having the given id from the given list of bookings.

    Parameters
    ----------
    bookings : list[dict]
        The list of bookings.
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

    Returns
    -------
    list[dict]:
        A new list of bookings containing copies of the bookings in the given list, where the copy of the one to edit
        has been modified accordingly.
    """
    new_bookings = []
    for booking in bookings:
        if booking_get_id(booking) == id_:
            # we add a booking with the updated attributes in place of the original one
            new_booking = booking_create(id_, new_name, new_class_type, new_price, new_checked_in)
            new_bookings.append(new_booking)
        else:
            # if the ID's to do not match, keep the old booking
            new_bookings.append(booking)

    return new_bookings


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


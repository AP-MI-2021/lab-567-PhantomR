def booking_create(id_: int, name: str, class_type: str, price: float, checked_in: bool) -> dict:
    """
    Creates a Booking entity using the given attributes.

    Parameters
    ----------
    id_ : int
        The booking's ID.
    name : str
        The booking's name.
    class_type : str
        The booking's class: "Economy", "Economy Plus" or "Business".
    price : float
        The booking's price.
    checked_in : bool
        Specifies whether this booking was checked in.

    Returns
    -------
    dict
    A dictionary encompassing the created Booking entity.
    """

    # TODO: TYPE-HINT THE DICTIONARY!

    return {
        "id": id_,
        "name": name,
        "class_type": class_type,
        "price": price,
        "checked_in": checked_in
    }


def booking_get_id(booking: dict) -> int:
    """
    Returns the value of the Booking's ID attribute.

    Parameters
    ----------
    booking : dict
        The Booking whose ID we are returning.

    Returns
    -------
    int
        The value of the Booking's ID attribute.
    """
    return booking["id"]


def booking_set_id(booking: dict, id_: int):
    # TODO: WRITE DOCSTRING
    booking["id"] = id_


def booking_get_name(booking: dict) -> str:
    # TODO: WRITE DOCSTRING
    return booking["name"]


def booking_set_name(booking: dict, name: str):
    # TODO: WRITE DOCSTRING
    booking["name"] = name


def booking_get_class_type(booking: dict) -> str:
    # TODO: WRITE DOCSTRING
    return booking["class_type"]


def booking_set_class_type(booking: dict, class_type: str):
    # TODO: WRITE DOCSTRING
    booking["class_type"] = class_type


def booking_get_price(booking: dict) -> float:
    # TODO: WRITE DOCSTRING
    return booking["price"]


def booking_set_price(booking: dict, price: float):
    # TODO: WRITE DOCSTRING
    booking["price"] = price


def booking_get_checked_in(booking: dict) -> bool:
    # TODO: WRITE DOCSTRING
    return booking["checked_in"]


def booking_set_id(booking: dict, checked_in: bool):
    # TODO: WRITE DOCSTRING
    booking["checked_in"] = checked_in



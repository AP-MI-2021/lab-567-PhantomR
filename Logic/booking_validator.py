from typing import Tuple


def booking_validate_id(id_) -> int:
    errors = []
    if id_ == '':
        errors.append('ID cannot be empty.')
    try:
        id_ = int(id_)
        if id_ < 0:
            errors.append('ID must be non-negative.')
    except ValueError:
        errors.append('ID must be an integer.')

    if len(errors) != 0:
        raise ValueError(errors)

    return id_


def booking_validate(id_, name, class_type, price, checked_in) -> Tuple[int, str, str, float, bool]:
    """
    Validates the fields of a Booking entity.

    Parameters
    ----------
    id_ : str
        The entity's ID.
    name : str
        The entity's name.
    class_type : str
        The entity's class type.
    price : str
        The entity's price.
    checked_in : str
        A string specifying whether the booking was checked in (Y) or not (N).

    Returns
    -------

    """
    errors = []

    # validate ID
    if id_ == '':
        errors.append('ID cannot be empty.')
    try:
        id_ = int(id_)
        if id_ < 0:
            errors.append('ID must be non-negative.')
    except ValueError:
        errors.append('ID must be an integer.')

    # validate name
    if name == '':
        errors.append('Name cannot be empty.')

    # validate class_type
    if class_type == '':
        errors.append('Class Type cannot be empty.')
    if class_type not in ['Economy', 'Economy Plus', 'Business']:
        errors.append('Class Type can only be one of Economy, Economy Plus and Business')

    # validate price
    try:
        price = float(price)
        if price < 0:
            errors.append('Price must be non-negative.')
    except ValueError:
        errors.append('Price must be a real number.')

    # validate checked_in
    if checked_in not in ['Y', 'N']:
        errors.append('Checked in can only be Y or N.')
    else:
        checked_in = True if checked_in == 'Y' else False

    if len(errors) != 0:
        raise ValueError(errors)

    return id_, name, class_type, price, checked_in

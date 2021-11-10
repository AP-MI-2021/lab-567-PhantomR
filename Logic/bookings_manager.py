from copy import deepcopy


def bookings_manager_create() -> dict:
    """
    Creates a new Bookings Manager.

    Returns
    -------
    dict:
        A dictionary representing a Bookings Manager.

    """
    return {
        'undo_lists': [],
        'current_list': [],
        'redo_lists': [],
    }


def bookings_manager_get_undo_lists(bookings_manager: dict) -> list:
    return bookings_manager['undo_lists']


def bookings_manager_get_current_list(bookings_manager: dict) -> list:
    return bookings_manager['current_list']


def bookings_manager_get_redo_lists(bookings_manager: dict) -> list:
    return bookings_manager['redo_lists']


def bookings_manager_get_can_redo(bookings_manager: dict) -> bool:
    return bookings_manager['can_redo']


def bookings_manager_set_current_list(bookings_manager: dict, new_current_list: list):
    bookings_manager['current_list'] = new_current_list


def bookings_manager_add_redo(bookings_manager: dict):
    current_list_copy = deepcopy(bookings_manager_get_current_list(bookings_manager))
    redo_lists = bookings_manager_get_redo_lists(bookings_manager)
    redo_lists.append(current_list_copy)


def bookings_manager_add_undo(bookings_manager: dict):
    current_list_copy = deepcopy(bookings_manager_get_current_list(bookings_manager))
    undo_lists = bookings_manager_get_undo_lists(bookings_manager)
    undo_lists.append(current_list_copy)


def bookings_manager_clear_redo_lists(bookings_manager: dict):
    undo_lists = bookings_manager_get_redo_lists(bookings_manager)
    undo_lists.clear()


def bookings_manager_record_modification(bookings_manager: dict):
    """
    Stores the previous current list into the undo lists in preparation for its modification.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager we operate on.
    """
    bookings_manager_add_undo(bookings_manager)
    bookings_manager_clear_redo_lists(bookings_manager)


def bookings_manager_apply_undo(bookings_manager: dict):
    """
    Performs an UNDO operation, if possible.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager we operate on.

    Returns
    ----------
    bool:
        True if there was an operation to undo, False otherwise.
    """
    undo_lists = bookings_manager_get_undo_lists(bookings_manager)
    if len(undo_lists) >= 1:
        # store current list into redo
        bookings_manager_add_redo(bookings_manager)

        # remove the previous list from the undo lists
        previous_list = undo_lists.pop()

        # set the previous list to be the current one
        bookings_manager_set_current_list(bookings_manager, previous_list)

        return True

    return False


def bookings_manager_apply_redo(bookings_manager: dict) -> bool:
    """
    Performs a REDO operation, if possible.

    Parameters
    ----------
    bookings_manager : dict
        The Bookings Manager we operate on.

    Returns
    ----------
    bool:
        True if there was an operation to redo, False otherwise.
    """
    redo_lists = bookings_manager_get_redo_lists(bookings_manager)
    if len(redo_lists) >= 1:
        # store current list into undo
        bookings_manager_add_undo(bookings_manager)

        # remove the next list from the redo lists
        next_list = redo_lists.pop()

        # set the previous list to be the current one
        bookings_manager_set_current_list(bookings_manager, next_list)

        return True

    return False

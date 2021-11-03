from Logic.booking_crud import *
from Logic.booking_validator import booking_validate, booking_validate_id
from Logic.bookings_general import *


def ui_show_main_menu():
    print('''
    MAIN MENU
    -------------------------------------------
    1. Create / Read / Update / Delete Bookings
    2. Other operations on Bookings
    3. Undo / Redo
    -------------------------------------------
    0. Exit
    ''')


def print_list(exc):
    print(exc)



def ui_show_crud_menu():
    print('''
    CRUD MENU
    -------------------------------------------
    1. Create a new Booking
    2. Display all Bookings
    3. Edit a Booking
    4. Delete a Booking
    -------------------------------------------
    0. Go back to the Main Menu
    ''')


def ui_show_other_operations_menu():
    print('''
    OTHER OPERATIONS MENU
    -------------------------------------------
    1. Sort bookings in decreasing order by price
    2. Find the maximum price for all class types
    -------------------------------------------
    0. Go back to the Main Menu    
    ''')


def ui_run_main_menu_loop(bookings):
    while True:
        ui_show_main_menu()
        option = int(input("What would you like to do? "))
        if option == 1:
            bookings = ui_run_crud_menu_loop(bookings)
        elif option == 2:
            bookings = ui_run_other_operations_menu(bookings)
        elif option == 3:
            ui_run_undo_redo_menu()
        elif option == 0:
            break
        else:
            print("Invalid operation number. Please try again.")

    return bookings


def ui_handle_create_new_booking(bookings):
    id_ = input("Enter the new booking's ID: ")
    name = input("Enter the new booking's name: ")
    # TODO: Make a menu for this
    class_type = input("Enter the new booking's class type (Economy, Economy Plus or Business: ")
    price = input("Enter the new booking's price: ")
    # TODO: Make a menu for this
    checked_in = input("Is this booking checked in (Y/N)? ")
    try:
        id_, name, class_type, price, checked_in = booking_validate(id_, name, class_type, price, checked_in)
    except ValueError as e:
        print_list(e)

    return crud_insert_booking(bookings, id_, name, class_type, price, checked_in)


def ui_handle_display_all_existing_bookings(bookings):
    # TODO: Add some variables, dirty calls inside the format string
    if len(bookings) == 0:
        print("There are no bookings to show.")
    else:
        print("Here's a list of all bookings: ")

        for booking in bookings:
            print(f'''
            ----------------------------------------------
            ID: {booking_get_id(booking)}
            Name: {booking_get_name(booking)}
            Class Type: {booking_get_class_type(booking)}
            Price: {booking_get_price(booking)}
            Checked In: {booking_get_checked_in(booking)}
            ----------------------------------------------
            
            ''')


def ui_edit_existing_booking(bookings):
    new_bookings = bookings

    id_ = int(input("Enter the booking's ID: "))
    try:
        booking_validate_id(id_)
    except ValueError as e:
        print_list(e)

    if crud_get_booking(bookings, int(id_)) is None:
        print("A booking with the given id does not exist.")
    else:
        new_name = input("Enter the new booking's name: ")
        # TODO: Make a menu for this
        new_class_type = input("Enter the new booking's class type (Economy, Economy Plus or Business: ")
        new_price = input("Enter the new booking's price: ")
        new_checked_in = input("Is the booking checked in? (Y/N)")
        # TODO: Make a menu for this

        try:
            id_, new_name, new_class_type, new_price, new_checked_in = \
                booking_validate(str(id_), new_name, new_class_type, new_price, new_checked_in)

            new_bookings = crud_edit_booking(bookings, id_, new_name, new_class_type, new_price, new_checked_in)
            print("Booking successfully edited.")
        except ValueError as e:
            print_list(e)

    return new_bookings


def ui_delete_existing_booking(bookings):
    new_bookings = bookings
    id_ = input("Enter the booking's ID: ")
    try:
        booking_validate_id(id_)
        booking = crud_get_booking(bookings, int(id_))
        try:
            if booking is None:
                print("A booking with the given id does not exist.")
            else:
                new_bookings = crud_delete_booking(bookings, id_)
                print("Booking successfully deleted.")

        except ValueError as e:
            print_list(e)

    except ValueError as e:
        print_list(e)

    return new_bookings


def ui_run_crud_menu_loop(bookings):
    while True:
        ui_show_crud_menu()
        option = int(input("What would you like to do? "))
        if option == 1:
            bookings = ui_handle_create_new_booking(bookings)
        elif option == 2:
            ui_handle_display_all_existing_bookings(bookings)
        elif option == 3:
            bookings = ui_edit_existing_booking(bookings)
        elif option == 4:
            bookings = ui_delete_existing_booking(bookings)
        elif option == 0:
            break
        else:
            print("Invalid operation number. Please try again.")

    return bookings


def ui_handle_sort_bookings_decreasingly_by_price(bookings):
    bookings = bookings_general_sort_decreasingly_by_price(bookings)
    print("Done sorting.")
    ui_handle_display_all_existing_bookings(bookings)
    return bookings


def ui_find_maximum_price_for_all_class_types(bookings):
    max_economy = bookings_general_find_maximum_price_for_class_type(bookings, "Economy")
    max_economy_plus = bookings_general_find_maximum_price_for_class_type(bookings, "Economy Plus")
    max_business = bookings_general_find_maximum_price_for_class_type(bookings, "Business")

    print(f"The maximum price for the Economy class is {max_economy}")
    print(f"The maximum price for the Economy Plus class is {max_economy_plus}")
    print(f"The maximum price for the Business class is {max_business}")


def ui_run_other_operations_menu(bookings):
    while True:
        ui_show_other_operations_menu()
        option = int(input("What would you like to do? "))
        if option == 1:
            bookings = ui_handle_sort_bookings_decreasingly_by_price(bookings)
        elif option == 2:
            ui_find_maximum_price_for_all_class_types(bookings)
        elif option == 0:
            break
        else:
            print("Invalid operation number. Please try again.")

    return bookings


def ui_run_undo_redo_menu():
    pass

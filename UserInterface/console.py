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
    3. Compute the total price of bookings under a given name
    4. Discount checked in bookings by a given percentage
    5. Upgrade class type of bookings under a given name to a superior one
    -------------------------------------------
    0. Go back to the Main Menu    
    ''')


def ui_show_undo_redo_menu():
    print('''
    UNDO / REDO MENU
    -------------------------------------------
    1. Undo
    2. Redo
    -------------------------------------------
    0. Go back to the Main Menu    
    ''')


def ui_run_main_menu_loop(bookings_manager):
    while True:
        ui_show_main_menu()
        try:
            option = int(input("What would you like to do? "))
            if option == 1:
                ui_run_crud_menu_loop(bookings_manager)
            elif option == 2:
                ui_run_other_operations_menu(bookings_manager)
            elif option == 3:
                ui_run_undo_redo_menu(bookings_manager)
            elif option == 0:
                break
            else:
                print("Invalid operation number. Please try again.")
        except ValueError:
            print("Option must be an integer. Please try again.")


def ui_handle_create_new_booking(bookings_manager):
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

    crud_insert_booking(bookings_manager, id_, name, class_type, price, checked_in)


def ui_handle_display_all_existing_bookings(bookings_manager):
    # TODO: Add some variables, dirty calls inside the format string
    bookings = bookings_manager_get_current_list(bookings_manager)
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


def ui_edit_existing_booking(bookings_manager):

    id_ = int(input("Enter the booking's ID: "))
    try:
        booking_validate_id(id_)
    except ValueError as e:
        print_list(e)

    if crud_get_booking(bookings_manager_get_current_list(bookings_manager), int(id_)) is None:
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

            crud_edit_booking(bookings_manager, id_, new_name, new_class_type, new_price, new_checked_in)
            print("Booking successfully edited.")
        except ValueError as e:
            print_list(e)


def ui_delete_existing_booking(bookings_manager):
    id_ = input("Enter the booking's ID: ")
    try:
        id_ = booking_validate_id(id_)
        booking = crud_get_booking(bookings_manager_get_current_list(bookings_manager), id_)
        try:
            if booking is None:
                print("A booking with the given id does not exist.")
            else:
                crud_delete_booking(bookings_manager, id_)
                print("Booking successfully deleted.")

        except ValueError as e:
            print_list(e)

    except ValueError as e:
        print_list(e)


def ui_run_crud_menu_loop(bookings_manager):
    while True:
        ui_show_crud_menu()
        try:
            option = int(input("What would you like to do? "))
            if option == 1:
                ui_handle_create_new_booking(bookings_manager)
            elif option == 2:
                ui_handle_display_all_existing_bookings(bookings_manager)
            elif option == 3:
                ui_edit_existing_booking(bookings_manager)
            elif option == 4:
                ui_delete_existing_booking(bookings_manager)
            elif option == 0:
                break
            else:
                print("Invalid operation number. Please try again.")
        except ValueError:
            print("Option must be an integer. Please try again.")


def ui_handle_sort_bookings_decreasingly_by_price(bookings_manager):
    bookings_general_sort_decreasingly_by_price(bookings_manager)
    print("Done sorting.")
    ui_handle_display_all_existing_bookings(bookings_manager)


def ui_find_maximum_price_for_all_class_types(bookings_manager):
    bookings = bookings_manager_get_current_list(bookings_manager)
    max_economy = bookings_general_find_maximum_price_for_class_type(bookings, "Economy")
    max_economy_plus = bookings_general_find_maximum_price_for_class_type(bookings, "Economy Plus")
    max_business = bookings_general_find_maximum_price_for_class_type(bookings, "Business")

    print(f"The maximum price for the Economy class is {max_economy}")
    print(f"The maximum price for the Economy Plus class is {max_economy_plus}")
    print(f"The maximum price for the Business class is {max_business}")


def ui_handle_compute_total_price_of_bookings_for_name(bookings_manager):
    name = input("Input a name: ")
    total_price_of_bookings_under_give_name = bookings_general_compute_total_price_of_bookings_for_name(bookings_manager, name)
    if total_price_of_bookings_under_give_name == -1:
        print("Name not found in any booking.")
    else:
        print("The total price of the bookings under the given nanme is " + str(total_price_of_bookings_under_give_name))


def ui_handle_discount_checked_in_bookings_by_given_percentage(bookings_manager):
    try:
        discount_percentage = int(input("Input a discount percentage (an integer between 1 and 100): "))
        if (discount_percentage < 1) or (discount_percentage > 100):
            print("Discount must be an integer between 1 and 100.")
        else:
            bookings_general_discount_checked_in_bookings(bookings_manager, discount_percentage)
            print("Discounts applied successfully.")
    except ValueError:
        print("Discount percentage must be an integer.")


def ui_handle_upgrade_class_type_of_bookings_for_name(bookings_manager):
    name = input("Input a name: ")
    bookings_general_upgrade_class_type_of_bookings_for_name(bookings_manager, name)
    print("Class type upgrade completed successfully")


def ui_run_other_operations_menu(bookings_manager):
    while True:
        ui_show_other_operations_menu()
        try:
            option = int(input("What would you like to do? "))
            if option == 1:
                ui_handle_sort_bookings_decreasingly_by_price(bookings_manager)
            elif option == 2:
                ui_find_maximum_price_for_all_class_types(bookings_manager)
            elif option == 3:
                ui_handle_compute_total_price_of_bookings_for_name(bookings_manager)
            elif option == 4:
                ui_handle_discount_checked_in_bookings_by_given_percentage(bookings_manager)
            elif option == 5:
                ui_handle_upgrade_class_type_of_bookings_for_name(bookings_manager)
            elif option == 0:
                break
            else:
                print("Invalid operation number. Please try again.")
        except ValueError:
            print("Option must be an integer. Please try again.")


def ui_handle_undo(bookings_manager):
    was_successful = bookings_manager_apply_undo(bookings_manager)
    if was_successful:
        print("Undo operation successful.")
    else:
        print("Nothing to undo.")


def ui_handle_redo(bookings_manager):
    was_successful = bookings_manager_apply_redo(bookings_manager)
    if was_successful:
        print("Redo operation successful.")
    else:
        print("Nothing to redo.")


def ui_run_undo_redo_menu(bookings_manager):
    while True:
        ui_show_undo_redo_menu()
        try:
            option = int(input("What would you like to do? "))
            if option == 1:
                ui_handle_undo(bookings_manager)
            elif option == 2:
                ui_handle_redo(bookings_manager)
            elif option == 0:
                break
            else:
                print("Invalid operation number. Please try again.")
        except ValueError:
            print("Option must be an integer. Please try again.")


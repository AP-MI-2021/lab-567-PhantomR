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


def ui_run_main_menu_loop(bookings):
    while True:
        ui_show_main_menu()
        option = int(input("What would you like to do? "))
        if option == 1:
            bookings = ui_run_crud_menu_loop(bookings)
        elif option == 2:
            ui_run_other_operations_menu()
        elif option == 3:
            ui_run_undo_redo_menu()
        elif option == 0:
            break
        else:
            print("Invalid operation number. Please try again.")

    return bookings


def ui_handle_create_new_booking(bookings):
    new_bookings = []
    return new_bookings


def ui_handle_display_all_existing_bookings(bookings):
    new_bookings = []
    return new_bookings


def ui_edit_existing_booking(bookings):
    new_bookings = []
    return new_bookings


def ui_delete_existing_booking(bookings):
    new_bookings = []
    return new_bookings


def ui_run_crud_menu_loop(bookings):
    while True:
        ui_show_crud_menu()
        option = int(input("What would you like to do? "))
        if option == 1:
            bookings = ui_handle_create_new_booking(bookings)
        elif option == 2:
            bookings = ui_handle_display_all_existing_bookings(bookings)
        elif option == 3:
            bookings = ui_edit_existing_booking(bookings)
        elif option == 4:
            bookings = ui_delete_existing_booking(bookings)
        elif option == 0:
            break
        else:
            print("Invalid operation number. Please try again.")

    return bookings


def ui_run_other_operations_menu():
    pass


def ui_run_undo_redo_menu():
    pass


from Logic.bookings_manager import bookings_manager_create
from UserInterface.console import ui_run_main_menu_loop
# from UserInterface.command_line_console import command_line_console_run_ui
from Tests.run_tests import run_all_tests
from Logic.booking_crud import crud_insert_booking


def main():
    run_all_tests()

    bookings_manager = bookings_manager_create()
    crud_insert_booking(bookings_manager, 1, "Alexandru Duna", "Economy", 100.0, True)
    crud_insert_booking(bookings_manager, 2, "Ion Pisoi", "Economy Plus", 200.0, False)
    crud_insert_booking(bookings_manager, 3, "Bill Tractor", "Business", 500.0, True)
    crud_insert_booking(bookings_manager, 4, "Cosmin Piersica", "Business", 1000.0, True)
    crud_insert_booking(bookings_manager, 5, "Ion Pisoi", "Economy", 50.0, False)

    ui_run_main_menu_loop(bookings_manager)
    # command_line_console_run_ui(bookings)


if __name__ == "__main__":
    main()

from UserInterface.console import ui_run_main_menu_loop
from Tests.run_tests import run_all_tests

def main():
    run_all_tests()

    bookings = []
    ui_run_main_menu_loop(bookings)


if __name__ == "__main__":
    main()
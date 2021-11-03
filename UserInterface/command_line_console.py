from typing import Tuple
from Logic.booking_crud import *
from Logic.bookings_general import *


def command_line_console_show_help():
    print('''
    AVAILABLE COMMANDS:
    ==============================================================================================================
    COMMAND FORMAT                                   |  EFFECT
    --------------------------------------------------------------------------------------------------------------
    delete, ID                                       |  Deletes the Booking with the given ID.
    -------------------------------------------------|------------------------------------------------------------                                                     
    add,    ID, name, class type, price, Y/N         |  Inserts a Booking having the given attributes.
    -------------------------------------------------|------------------------------------------------------------
    showall                                          |  Lists all bookings.
    -------------------------------------------------|------------------------------------------------------------
    edit,   ID, name, class type, price, Y/N         |  Changes the attributes of the Booking having the given ID.
    -------------------------------------------------|------------------------------------------------------------
    exit                                             |  Exits the application.    
    -------------------------------------------------|------------------------------------------------------------
    ''')


def command_line_console_handle_add_command(bookings, command):
    command_fields = command.split(',')
    if len(command_fields) != 6:
        print("Invalid add command format.")

    id_ = int(command_fields[1])
    name = command_fields[2]
    class_type = command_fields[3]
    price = float(command_fields[4])
    checked_in = True if command_fields[4] == 'Y' else False

    return crud_insert_booking(bookings, id_, name, class_type, price, checked_in)


def command_line_console_handle_showall_command(bookings, command):
    command_fields = command.split(',')
    if len(command_fields) != 1:
        print("Invalid showall command format.")

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


def command_line_console_handle_edit_command(bookings, command):
    command_fields = command.split(',')
    if len(command_fields) != 6:
        print("Invalid edit command format.")

    new_bookings = bookings
    id_ = int(command_fields[1])
    if crud_get_booking(bookings, id_) is None:
        print("A booking with the given id does not exist.")
    else:
        new_name = command_fields[2]
        new_class_type = command_fields[3]
        new_price = float(command_fields[4])
        new_checked_in = True if command_fields[4] == 'Y' else False
        new_bookings = crud_edit_booking(bookings, id_, new_name, new_class_type, new_price, new_checked_in)
        print("Booking successfully edited.")

    return new_bookings


def command_line_console_handle_delete_command(bookings, command):
    command_fields = command.split(',')
    if len(command_fields) != 2:
        print("Invalid delete command format.")
    new_bookings = bookings
    id_ = int(command_fields[1])
    if crud_get_booking(bookings, id_) is None:
        print("A booking with the given id does not exist.")
    else:
        new_bookings = crud_delete_booking(bookings, id_)
        print("Booking successfully deleted.")

    return new_bookings


def parse_command(command: str, bookings: list[dict]) -> Tuple[list[dict], bool]:
    new_bookings = bookings

    command_fields = command.split(',')
    if len(command_fields) >= 1:
        command_name = command_fields[0]
        if command_name == "exit":
            return new_bookings, True
        elif command_name == "showall":
            command_line_console_handle_showall_command(bookings, command)
        elif command_name == "add":
            new_bookings = command_line_console_handle_add_command(bookings, command)
        elif command_name == "delete":
            new_bookings = command_line_console_handle_delete_command(bookings, command)
        elif command_name == "edit":
            new_bookings = command_line_console_handle_edit_command(bookings, command)
        else:
            print("Invalid command. Please try again.")

    return new_bookings, False


def parse_command_sequence(commands: str, bookings: list[dict]) -> Tuple[list[dict], bool]:
    new_bookings = bookings
    exit_program = False

    commands_list = commands.split(';')
    for command in commands_list:
        new_bookings, exit_program = parse_command(command, new_bookings)

    return new_bookings, exit_program


def command_line_console_run_ui(bookings):
    while True:
        command_line_console_show_help()
        commands = input("Enter the commands you want to run, separated by a semicolon: ")
        bookings, exit_program = parse_command_sequence(commands, bookings)
        if exit_program:
            break

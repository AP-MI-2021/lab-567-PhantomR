from Domain.booking import *


def test_booking_getters():
    booking = booking_create(1, "Alexandru Duna", "Economy", 100.0, True)

    # check if both the constructor and getters work
    assert booking_get_id(booking) == 1
    assert booking_get_name(booking) == "Alexandru Duna"
    assert booking_get_class_type(booking) == "Economy"
    assert booking_get_price(booking) == 100.0
    assert booking_get_checked_in(booking) is True


def test_booking_setters():
    booking = booking_create(1, "Alexandru Duna", "Economy", 100.0, True)

    # check if intitial Booking was created successfully
    assert booking_get_id(booking) == 1
    assert booking_get_name(booking) == "Alexandru Duna"
    assert booking_get_class_type(booking) == "Economy"
    assert booking_get_price(booking) == 100.0
    assert booking_get_checked_in(booking) is True

    # modify and check each attribute, one at a time
    booking_set_id(booking, 2)
    assert booking_get_id(booking) == 2
    booking_set_name(booking, "Alexandru Dan Duna")
    assert booking_get_name(booking) == "Alexandru Dan Duna"
    booking_set_class_type(booking, "Business")
    assert booking_get_class_type(booking) == "Business"
    booking_set_price(booking, 200.0)
    assert booking_get_price(booking) == 200.0
    booking_set_checked_in(booking, False)
    assert booking_get_checked_in(booking) is False

    # now check if all attributes were modified successfully
    assert booking_get_id(booking) == 2
    assert booking_get_name(booking) == "Alexandru Dan Duna"
    assert booking_get_class_type(booking) == "Business"
    assert booking_get_price(booking) == 200.0
    assert booking_get_checked_in(booking) is False


def run_booking_tests():
    test_booking_getters()
    test_booking_setters()
    print("[TESTS] All Booking tests ran successfully")





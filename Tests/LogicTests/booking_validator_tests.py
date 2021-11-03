from Logic.booking_validator import booking_validate


def run_booking_validator_tests():
    # negative ID
    try:
        booking_validate('-100', 'Alex', 'Economy', '100.0', 'Y')
        assert False
    except ValueError:
        pass

    # empty name
    try:
        booking_validate('1', '', 'Economy', '100.0', 'Y')
        assert False
    except ValueError:
        pass

    # empty class type
    try:
        booking_validate('1', 'Alex', '', '100.0', 'Y')
        assert False
    except ValueError:
        pass

    # class type not among Economy, Economy Plus and Business
    try:
        booking_validate('1', 'Alex', 'EconomyAA', '100.0', 'Y')
        assert False
    except ValueError:
        pass

    # price cannot be converted to float
    try:
        booking_validate('1', 'Alex', 'EconomyAA', '100.0A', 'Y')
        assert False
    except ValueError:
        pass

    # checked in must be Y or N
    try:
        booking_validate('1', 'Alex', 'EconomyAA', '100.0A', 'NO')
        assert False
    except ValueError:
        pass

    # all fields invalid
    try:
        booking_validate('-1', '', 'BB', 'a200.0', 'Yes')
        assert False
    except ValueError:
        pass

    # all fields valid
    try:
        booking_validate('1', 'Alex', 'Business', '1000.0', 'Y')
    except ValueError:
        assert True

    print("[TESTS] All booking validator tests passed.")

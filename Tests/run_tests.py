from Tests.DomainTests.booking_test import run_booking_tests
from Tests.LogicTests.booking_crud_tests import run_booking_crud_tests

def run_all_tests():
    run_booking_tests()
    run_booking_crud_tests()
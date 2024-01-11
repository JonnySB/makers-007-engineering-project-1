from lib.booking_request import BookingRequest
from datetime import date

"""
Initialises with given attributes
"""

def test_booking_request_initialises_with_given_attributes():
    booking_request = BookingRequest(99, 1, True, False, 1)
    assert booking_request.id == 99
    assert booking_request.guest_id == 1
    assert booking_request.pending == True
    assert booking_request.accepted == False
    assert booking_request.booking_id == 1


def test_booking_request_eq():
    booking_request1 = BookingRequest(99, 1, True, False, 1)
    booking_request2 = BookingRequest(99, 1, True, False, 1)
    assert booking_request1 == booking_request2


def test_booking_request_repr():
    booking_request = BookingRequest(99, 1, True, False, 1)
    assert str(booking_request) == "BookingRequest(99, 1, True, False, 1)"
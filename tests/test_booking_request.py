from lib.booking_request import BookingRequest
from datetime import date

"""
Initialises with given attributes
"""

def test_booking_request_initialises_with_given_attributes():
    booking_request = BookingRequest(99, 1, True, True, 1)
    assert booking_request.id == 99
    assert booking_request.guest_id == 1
    assert booking_request.pending == True
    assert booking_request.accepted == False
    assert booking_request.booking_id == 1


# def test_booking_eq():
#     date1 = BookingRequest(1, date(2023, 12, 5), True, 1)
#     date2 = BookingRequest(1, date(2023, 12, 5), True, 1)
#     assert date1 == date2


# def test_booking_repr():
#     date1 = BookingRequest(1, date(2023, 12, 5), True, 1)
#     assert str(date1) == "BookingRequest(1, 2023-12-05, True, 1)"
from lib.booking import Booking
from datetime import datetime

"""
Initialises with given attributes
"""

def test_initialises_with_given_attributes():
    date = Booking(1, datetime(2023, 12, 5), True, 1)
    assert date.id == 1
    assert date.date == datetime(2023, 12, 5)
    assert date.available == True
    assert date.space_id == 1


def test_booking_eq():
    date1 = Booking(1, datetime(2023, 12, 5), True, 1)
    date2 = Booking(1, datetime(2023, 12, 5), True, 1)
    assert date1 == date2

from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date


# test get bookings for space with certain id
def test_get_space_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_repository = BookingRepository(db_connection)

    rows = booking_repository.get_by_id(1)

    assert rows == [
        Booking(1, date(2024, 5, 10), True, 1),
        Booking(2, date(2024, 5, 11), False, 1),
        Booking(3, date(2024, 5, 12), False, 1),
    ]

def test_update_booking(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_repository = BookingRepository(db_connection)

    rows = booking_repository.get_by_id(1)

    assert rows == [
        Booking(1, date(2024, 5, 10), True, 1),
        Booking(2, date(2024, 5, 11), False, 1),
        Booking(3, date(2024, 5, 12), False, 1),
    ]

    # change first data value
    booking_repository.update_availability(1)

    rows = booking_repository.get_by_id(1)

    assert rows == [
        Booking(1, date(2024, 5, 10), False, 1),
        Booking(2, date(2024, 5, 11), False, 1),
        Booking(3, date(2024, 5, 12), False, 1),
    ]

"""
When I call #create
I create a booking in the bookings table
and can find it with #get_by_id
"""
def test_create_booking(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = BookingRepository(db_connection)
    booking = Booking(None, date(2024, 5, 13), True, 1)
    repository.create(booking)
    assert repository.get_by_id(1) == [
        Booking(1, date(2024, 5, 10), True, 1),
        Booking(2, date(2024, 5, 11), False, 1),
        Booking(3, date(2024, 5, 12), False, 1),
        Booking(13, date(2024, 5, 13), True, 1)
    ]
from lib.booking_repository import BookingRepository
from lib.booking import Booking


# test get bookings for space with certain id
def test_get_space_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_repository = BookingRepository(db_connection)

    rows = booking_repository.get_by_id(1)

    assert rows == [
        Booking(1, "2024-05-10", True, 1),
        Booking(2, "2024-05-11", False, 1),
        Booking(3, "2024-05-12", False, 1),
    ]

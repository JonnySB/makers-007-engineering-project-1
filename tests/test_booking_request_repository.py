from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository

def test_get_booking_booking_requests_for_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_requests_repository = BookingRequestRepository(db_connection)

    rows = booking_requests_repository.get_booking_requests_for_user(1)

    assert rows == [
        BookingRequest(1, 1, True, False, 1),
        BookingRequest(2, 1, True, False, 1),
        BookingRequest(3, 1, True, False, 1),
    ]

def test_create_booking_request(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_requests_repository = BookingRequestRepository(db_connection)

    booking_request = BookingRequest(97, 1, True, False, 1)
    booking_requests_repository.create_booking_request(booking_request)

    assert str(booking_request) == "BookingRequest(97, 1, True, False, 1)"


# def test_accept_booking_request(db_connection):
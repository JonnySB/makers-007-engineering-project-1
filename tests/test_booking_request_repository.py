from datetime import date
from lib.booking_repository import BookingRepository
from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository
def test_create_booking_request(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_requests_repository = BookingRequestRepository(db_connection)
    booking_request = BookingRequest(4, 1, True, False, 1)
    booking_requests_repository.create_booking_request(booking_request)
    rows = booking_requests_repository.get_booking_requests_for_user(1)
    assert rows == [
        BookingRequest(1, 1, True, False, 1),
        BookingRequest(2, 1, True, False, 1),
        BookingRequest(3, 1, True, False, 1),
        BookingRequest(4, 1, True, False, 1)
    ]
    assert str(booking_request) == "BookingRequest(4, 1, True, False, 1)"

    
def test_get_booking_booking_requests_for_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_requests_repository = BookingRequestRepository(db_connection)
    rows = booking_requests_repository.get_booking_requests_for_user(1)
    assert rows == [
        BookingRequest(1, 1, True, False, 1),
        BookingRequest(2, 1, True, False, 1),
        BookingRequest(3, 1, True, False, 1),
    ]


def test_accept_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_requests_repository = BookingRequestRepository(db_connection)
    booking_repository = BookingRepository(db_connection)
    booking_request = BookingRequest(4, 1, True, False, 8)
    booking_requests_repository.create_booking_request(booking_request)
    booking_requests_repository.accept_booking_request(4)
    booking = booking_repository.get_by_booking_id(8)
    assert booking.available == False


def test_reject_booking_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    booking_requests_repository = BookingRequestRepository(db_connection)
    booking_request = BookingRequest(4, 1, True, False, 8)
    booking_requests_repository.create_booking_request(booking_request)
    booking_requests_repository.reject_booking_request(4)
    rows = booking_requests_repository.get_booking_requests_for_user(1)
    assert rows == [
        BookingRequest(1, 1, True, False, 1),
        BookingRequest(2, 1, True, False, 1),
        BookingRequest(3, 1, True, False, 1),
        BookingRequest(4, 1, False, False, 8)
    ]
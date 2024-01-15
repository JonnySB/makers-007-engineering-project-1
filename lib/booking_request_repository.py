from lib.booking import Booking
from lib.booking_request import BookingRequest

class BookingRequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_booking_request(self, guest_id, booking_id):
        self._connection.execute(
            'INSERT INTO booking_requests (guest_id, pending, accepted, booking_id) VALUES (%s, %s, %s, %s)', 
            [guest_id, True, False, booking_id],
        )

    def get_booking_requests_for_user(self, user_id):
        rows = self._connection.execute(
            "SELECT * FROM booking_requests WHERE guest_id = %s ORDER BY id",
            [user_id],
        )
        booking_requests = []
        for row in rows:
            booking_requests.append(
                BookingRequest(
                    row["id"],
                    row["guest_id"],
                    row["pending"],
                    row["accepted"],
                    row["booking_id"],
                )
            )
        return booking_requests

    def accept_booking_request(self, booking_requests_id):
        self._connection.execute(
            "UPDATE booking_requests "
            "SET pending = FALSE "
            "WHERE id = %s",
            [booking_requests_id]
        )
        self._connection.execute(
            "UPDATE booking_requests "
            "SET accepted = TRUE "
            "WHERE id = %s",
            [booking_requests_id]
        )
        booking_id = self._connection.execute(
            "SELECT booking_id "
            "FROM booking_requests "
            "WHERE id = %s",
            [booking_requests_id]
        )[0]['booking_id']
        self._connection.execute(
            "UPDATE bookings "
            "SET available = FALSE "
            "WHERE id = %s",
            [booking_id]
        )

    def reject_booking_request(self, booking_requests_id):
        self._connection.execute(
            "UPDATE booking_requests "
            "SET pending = FALSE "
            "WHERE id = %s",
            [booking_requests_id]
        )
        booking_id = self._connection.execute(
            "SELECT booking_id "
            "FROM booking_requests "
            "WHERE id = %s",
            [booking_requests_id]
        )[0]['booking_id']
        self._connection.execute(
            "UPDATE bookings "
            "SET available = TRUE "
            "WHERE id = %s",
            [booking_id]
        )

    def get_all_booking_requests(self):
        rows = self._connection.execute(
            "SELECT * FROM booking_requests"
        )
        bookings = []
        for row in rows:
            bookings.append(
                BookingRequest(
                    row["id"],
                    row["guest_id"],
                    row["pending"],
                    row["accepted"],
                    row["booking_id"],
                )
            )
        return bookings

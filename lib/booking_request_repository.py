from lib.booking import Booking
from lib.booking_request import BookingRequest
from lib.booking_manager import BookingManager

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
    
    def get_bookings_by_user(self, user_id):
        user_bookings = self._connection.execute("SELECT booking_requests.id, spaces.name, users.username, bookings.date, booking_requests.pending, booking_requests.accepted"
                        " FROM booking_requests"
                        " JOIN users on booking_requests.guest_id = users.id"
                        " JOIN bookings on booking_requests.booking_id = bookings.id"
                        " JOIN spaces on bookings.space_id = spaces.id"
                        " WHERE spaces.user_id = %s"
                        " ORDER BY pending DESC, date", [user_id])
        bookings_to_return = []
        for booking in user_bookings:
            bookings_to_return.append(
                BookingManager(
                    booking["id"],
                    booking["name"],
                    booking["username"],
                    booking["date"],
                    booking["pending"],
                    booking["accepted"]
                )
            )
        return bookings_to_return

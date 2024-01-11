from flask import session
from lib.booking import Booking
from datetime import date


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_by_id(self, space_id):
        rows = self._connection.execute(
            "SELECT * FROM bookings WHERE space_id = %s ORDER BY id",
            [space_id],
        )

        bookings = []
        for row in rows:
            bookings.append(
                Booking(
                    row["id"],
                    row["date"],
                    row["available"],
                    row["space_id"],
                )
            )

        return bookings
    
    def update_availability(self, booking_id):
        self._connection.execute(
            "UPDATE bookings "
            "SET available = FALSE "
            "WHERE id = %s",
            [booking_id]
        )


    


   


    def get_booking_requests_for_user(self, user_id):
        rows = self._connection.execute(
            "SELECT * FROM bookings "
            "JOIN spaces ON bookings.space_id = spaces.id "
            "WHERE spaces.user_id = %s "
            "AND available = TRUE "
            "ORDER BY bookings.id",
            [user_id],
        )

        booking_requests = []
        for row in rows:
            booking_requests.append(
                Booking(
                    row["id"],
                    row["date"],
                    row["available"],
                    row["space_id"],
                )
            )

        return booking_requests

    def accept_booking_request(self, booking_id):
        self._connection.execute(
            "UPDATE bookings "
            "SET available = FALSE "
            "WHERE id = %s",
            [booking_id]
        )

    def deny_booking_request(self, booking_id):
        self._connection.execute(
            "DELETE FROM bookings "
            "WHERE id = %s",
            [booking_id]
        )

# Assume you have a method to get the logged-in user ID from the session
def get_logged_in_user_id():
    # Implement this method based on your session management
    return session.get('user_id')


# 1. Method to get booking requests for a specific user
# 2. Creation of HTML template for booking requests
# 3. Create route for html template
# 4. Testing Pytest for booking request method

# 5. Method to accept/deny a booking request (accept_booking_request, deny_booking_request)
# 6. Add logic to accept/deny booking request
# 7. Testing (pytest) for accept and deny logic

# 8. Adding booking request to the database (change sql file)



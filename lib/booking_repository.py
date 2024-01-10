from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_by_id(self, space_id):
        rows = self._connection.execute(
            "SELECT * FROM bookings WHERE space_id = %s ORDER BY id",
            [space_id],
        )

        bookings = []
        # print(rows)
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

# add route for 'details' in spaces page
# add html page for 'details'
# add route for 'rent' button that will:
    # updating the database
    # updating the 'available' field dynamically from the database
    # (optional) display a success message (maybe pop-up?)
    # (optional) gray out the row(s) with the unavailable date(s)
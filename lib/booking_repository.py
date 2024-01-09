from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_by_id(self, space_id):
        rows = self._connection.execute(
            "SELECT * FROM bookings WHERE id = %s",
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

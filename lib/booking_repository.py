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
    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (date, available, space_id) VALUES (%s, %s, %s) RETURNING id', 
            [booking.date, booking.available, booking.space_id]
        )
        row = rows[0]
        booking.id = row["id"]
        return booking
    
    def get_by_booking_id(self, id):
        rows = self._connection.execute(
            "SELECT * FROM bookings WHERE id = %s ",
            [id],
        )
        rows = rows[0]
        booking = Booking(rows["id"], rows["date"], rows["available"], rows["space_id"])
        return booking
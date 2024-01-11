from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection


    # 1. Method to get booking requests for a specific user
    
    def get_booking_requests_for_user(self, user_id):





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










# def get_logged_in_user_id():
#     return session.get('user_id')

# @app.route("/booking_requests", methods=["GET"])
# def get_booking_requests():
#     user_id = get_logged_in_user_id()
    
#     if user_id:
#         connection = get_flask_database_connection(app)
#         booking_repo = BookingRepository(connection)
#         booking_requests = booking_repo.get_booking_requests_for_user(user_id)
#         return render_template("booking_requests.html", booking_requests=booking_requests)
#     else:
#         # Redirect to login page if the user is not logged in
#         return redirect(url_for("login"))

# @app.route("/accept_booking/<int:booking_id>", methods=["GET"])
# def accept_booking(booking_id):
#     user_id = get_logged_in_user_id()
    
#     if user_id:
#         connection = get_flask_database_connection(app)
#         booking_repo = BookingRepository(connection)
#         booking_repo.accept_booking_request(booking_id)
#         return redirect(url_for("get_booking_requests"))
#     else:
#         # Redirect to login page if the user is not logged in
#         return redirect(url_for("login"))

# @app.route("/deny_booking/<int:booking_id>", methods=["GET"])
# def deny_booking(booking_id):
#     user_id = get_logged_in_user_id()
    
#     if user_id:
#         connection = get_flask_database_connection(app)
#         booking_repo = BookingRepository(connection)
#         booking_repo.deny_booking_request(booking_id)
#         return redirect(url_for("get_booking_requests"))
#     else:
#         # Redirect to login page if the user is not logged in
#         return redirect(url_for("login"))
import os
from flask import Flask, request, render_template, redirect, session, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.space import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import datetime, timedelta
from lib.booking_request_repository import BookingRequestRepository
from lib.space_repository import SpaceRepository
from psycopg2 import errors

# Create a new Flask app
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# == Your Routes Here ==

def get_user_details(connection):
    user_repo = UserRepository(connection)
    user_id = session.get('user_id', None)
    user_details = None
    if user_id != None:
        user_details = user_repo.get_user_details(user_id)
    return user_details

@app.route("/")
def set_default_route():
    return redirect("/spaces")

@app.route("/reseed")
def reseed_database():
    connection = get_flask_database_connection(app)
    connection.connect()
    connection.seed("seeds/makers_bnb.sql")
    return redirect("/spaces")

# 'Homepage'
@app.route("/spaces", methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)

    spaces = space_repo.all()

    logged_in = session.get('logged_in', False)
    user_details = get_user_details(connection)

    return render_template("spaces/spaces.html", spaces=spaces, logged_in=logged_in, user=user_details)


@app.route("/spaces/new", methods=['GET'])
def get_new_space():
    connection = get_flask_database_connection(app)

    logged_in = session.get('logged_in', False)
    user_details = get_user_details(connection)

    return render_template('spaces/new.html', logged_in=logged_in, user=user_details)

@app.route("/spaces", methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    booking_repository = BookingRepository(connection)

    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    available_from = request.form['available_from']
    available_to = request.form['available_to']

    user_details = get_user_details(connection)

    space = Space(None, name, description, price, user_details.id) # needs to include user_id once login functionality added
    space = space_repository.create(space)

    available_from = datetime.strptime(available_from, '%Y-%m-%d')
    available_to = datetime.strptime(available_to, '%Y-%m-%d')
    current_date = available_from
    while current_date <= available_to:
        booking = Booking(None, current_date, True, space.id)
        booking = booking_repository.create(booking)
        current_date += timedelta(days=1)

    return redirect(f"/spaces")


@app.route("/spaces/<id>", methods=["GET"])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    booking_repo = BookingRepository(connection)
    space = space_repo.find(id)
    bookings = booking_repo.get_by_id(id)

    logged_in = session.get('logged_in', False)
    user_details = get_user_details(connection)

    return render_template("space.html", space=space, bookings=bookings, logged_in=logged_in, user=user_details)


# @app.route("/spaces/rent/<booking_id>/<space_id>", methods=["GET"])
# def rent_space(booking_id, space_id):
#     connection = get_flask_database_connection(app)
#     booking_repo = BookingRepository(connection)
#     booking_repo.update_availability(booking_id)
#     return redirect(f"/spaces/{space_id}")

@app.route("/space/rent/<booking_id>/<space_id>", methods=["POST"])
def create_booking_request(booking_id, space_id):
    connection = get_flask_database_connection(app)
    request_repo = BookingRequestRepository(connection)

    current_user = get_user_details(connection)
    guest_id = current_user.id

    try:
        request_repo.create_booking_request(guest_id, booking_id)
        flash("Booking request sent successfully!", "success")
    except errors.UniqueViolation:
        flash("You already sent a booking request for this date", "error")

    return redirect(f"/spaces/{space_id}")

    # try:
    #     request_repo.create_booking_request(guest_id, booking_id)
    # except errors.UniqueViolation:
    #     flash("You already sent a booking request for this date", "error")
    #     return redirect(f"/spaces/{space_id}")

    # return redirect(f"/spaces/{space_id}")


@app.route("/signup", methods=["GET"])
def get_user_info():
    return render_template("user_signup.html")


@app.route("/add_user", methods=["POST"])
def add_user_to_db():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    # confirm_password

    user = User(None, username, email, password)

    user = user_repository.create(user)
    return redirect("/login")


@app.route("/login", methods=["GET"])
def render_login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    username = request.form["user"]
    password = request.form["password"]

    # Check if user is in db and password matches
    user_id = user_repository.verify_user_login(username, password)

    # If the user can't be found:
    if not user_id:
        return render_template("login.html", errors="Incorrect login details")
    
    session['user_id'] = user_id
    session['logged_in'] = True

    return redirect("/spaces")

@app.route("/logout", methods=["GET"])
def logout_user():
    session['user_id'] = None
    session['logged_in'] = False
    return redirect(f"/spaces")

@app.route("/manage_bookings", methods=["GET"])
def get_booking_requests_for_user():
    connection = get_flask_database_connection(app)
    request_repo = BookingRequestRepository(connection)

    user_details = get_user_details(connection)
    bookings = request_repo.get_bookings_by_user(user_details.id)
    logged_in = session.get('logged_in', False)
    print(bookings)

    return render_template("booking_requests_new.html", logged_in=logged_in, bookings=bookings, user=user_details)

def get_booking_requests():
    connection = get_flask_database_connection(app)
    request_repo = BookingRequestRepository(connection)
    booking_repo = BookingRepository(connection)
    space_repo = SpaceRepository(connection)
    user_repo = UserRepository(connection)
    
    # will have selected booking requests based on the current_user
    all_requests = request_repo.get_all_booking_requests()
    requests = []

    logged_in = session.get('logged_in', False)

    if logged_in:
        # all spaces of the current_user
        all_spaces = space_repo.all()
        spaces = []

        # only get the requests for the current user spaces
        user_details = get_user_details(connection)
        current_user = user_details
        users = user_repo.all()

        for space in all_spaces:
            if space.user_id == current_user.id:
                spaces.append(space)
        
        all_spaces_bookings = []
        for space in spaces:
            all_spaces_bookings.append(booking_repo.get_by_id(space.id))

        bookings = []
        for space in all_spaces_bookings:
            for booking in space:
                bookings.append(booking)
        
        bookings = list(filter(None, bookings))

        for booking in bookings:
            for request in all_requests:
                if booking.id == request.booking_id:
                    requests.append(request)

        return render_template("booking_requests.html", requests = requests, bookings=bookings, logged_in=logged_in, current_user=current_user, spaces=spaces, users=users)
    else:
        return redirect("/login")
    
@app.route("/manage_bookings/accept/<booking_requests_id>", methods=["POST"])
def accept_request(booking_requests_id):
    connection = get_flask_database_connection(app)
    request_repo = BookingRequestRepository(connection)
    request_repo.accept_booking_request(booking_requests_id)
    return redirect("/manage_bookings")

@app.route("/manage_bookings/reject/<booking_requests_id>", methods=["POST"])
def reject_request(booking_requests_id):
    connection = get_flask_database_connection(app)
    request_repo = BookingRequestRepository(connection)
    request_repo.reject_booking_request(booking_requests_id)
    return redirect("/manage_bookings")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

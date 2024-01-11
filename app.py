import os
from flask import Flask, request, render_template,redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.space import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import datetime, timedelta

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route("/spaces", methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    spaces = space_repo.all()
    return render_template("spaces/spaces.html", spaces=spaces)

@app.route("/spaces/new", methods=['GET'])
def get_new_space():
    return render_template('spaces/new.html')

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

    space = Space(None, name, description, price, None) # needs to include user_id once login functionality added
    space = space_repository.create(space)

    available_from = datetime.strptime(available_from, '%Y-%m-%d')
    available_to = datetime.strptime(available_to, '%Y-%m-%d')
    current_date = available_from
    while current_date <= available_to:
        booking = Booking(None, current_date, True, space.id)
        booking = booking_repository.create(booking)
        current_date += timedelta(days=1)

    return redirect(f"/spaces")

@app.route("/spaces/<id>", methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    booking_repo = BookingRepository(connection)
    space = space_repo.find(id)
    bookings = booking_repo.get_by_id(id)
    return render_template("space.html", space=space, bookings=bookings)

@app.route("/spaces/rent/<booking_id>/<space_id>", methods=['GET'])
def rent_space(booking_id, space_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.update_availability(booking_id)
    return redirect(f"/spaces/{space_id}")

@app.route("/signup", methods=["GET"])
def get_user_info():
    return render_template("user_signup.html")

@app.route("/add_user", methods=["POST"])
def add_user_to_db():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    username = request.form["username"]
    email = request.form["email"]

    user = User(None, username, email)

    user = user_repository.create(user)
    return redirect(f"/spaces")





from flask import Flask, render_template, redirect, url_for, session



# Assume you have a method to get the logged-in user ID from the session
def get_logged_in_user_id():
    return session.get('user_id')

@app.route("/booking_requests", methods=["GET"])
def get_booking_requests():
    user_id = get_logged_in_user_id()
    
    if user_id:
        connection = get_flask_database_connection(app)
        booking_repo = BookingRepository(connection)
        booking_requests = booking_repo.get_booking_requests_for_user(user_id)
        return render_template("booking_requests.html", booking_requests=booking_requests)
    else:
        # Redirect to login page if the user is not logged in
        return redirect(url_for("login"))

@app.route("/accept_booking/<int:booking_id>", methods=["GET"])
def accept_booking(booking_id):
    user_id = get_logged_in_user_id()
    
    if user_id:
        connection = get_flask_database_connection(app)
        booking_repo = BookingRepository(connection)
        booking_repo.accept_booking_request(booking_id)
        return redirect(url_for("get_booking_requests"))
    else:
        # Redirect to login page if the user is not logged in
        return redirect(url_for("login"))

@app.route("/deny_booking/<int:booking_id>", methods=["GET"])
def deny_booking(booking_id):
    user_id = get_logged_in_user_id()
    
    if user_id:
        connection = get_flask_database_connection(app)
        booking_repo = BookingRepository(connection)
        booking_repo.deny_booking_request(booking_id)
        return redirect(url_for("get_booking_requests"))
    else:
        # Redirect to login page if the user is not logged in
        return redirect(url_for("login"))










@app.route("/booking_requests", methods=["GET"])
def get_booking_requests():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_requests = booking_repo.get_all_booking_requests()
    return render_template("booking_requests.html", booking_requests=booking_requests)

@app.route("/accept_booking/<int:booking_id>", methods=["GET"])
def accept_booking(booking_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.accept_booking_request(booking_id)
    return redirect(url_for("get_booking_requests"))

@app.route("/deny_booking/<int:booking_id>", methods=["GET"])
def deny_booking(booking_id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.deny_booking_request(booking_id)
    return redirect(url_for("get_booking_requests"))






# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))

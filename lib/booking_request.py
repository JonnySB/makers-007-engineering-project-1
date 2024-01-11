class BookingRequest:
    def __init__(self, id, guest_id, pending=True, accepted=False, booking_id=None):
        self.id = id
        self.guest_id = guest_id
        self.pending = pending
        self.accepted = accepted
        self.booking_id = booking_id

    # ensure two object with identical attributes will be found equal
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # return nicely formatted string version of object
    def __repr__(self):
        return f"BookingRequest({self.id}, {self.guest_id}, {self.pending}, {self.accepted}, {self.booking_id})"



# 1. Method to get booking requests for a specific user
# 2. Creation of HTML template for booking requests and add routes
# 3. Create route for html template
# 4. Testing Pytest for booking request method

# 5. Method to accept/deny a booking request (accept_booking_request, deny_booking_request)
# 6. Add logic to accept/deny booking request
# 7. Add switch between pending / accepted / declined 
# 8. Testing (pytest) for accept and deny logic

# 9. Adding booking_requests to the database (change sql file)
    
# extra: add create_booking_request method
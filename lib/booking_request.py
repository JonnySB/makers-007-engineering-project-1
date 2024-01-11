class BookingRequest:
    def __init__(self, id, guest_id, pending, accepted, booking_id):
        self.id = id
        self.guest_id = guest_id
        self.pending = pending
        self.accepted = accepted
        self.booking_id = booking_id

    # ensure two object with identical attrs will be found equal
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # return nicely formatted string version of peep object
    def __repr__(self):
        return f"BookingRequest({self.id}, {self.guest_id}, {self.pending}, {self.accepted}, {self.booking_id})"

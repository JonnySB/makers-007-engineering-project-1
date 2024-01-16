class BookingManager:
    def __init__(self, id, space, guest, date, pending, accepted):
        self.id = id
        self.space = space
        self.guest = guest
        self.date = date
        self.pending = pending
        self.accepted = accepted

    # ensure two object with identical attrs will be found equal
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # return nicely formatted string version of peep object
    def __repr__(self):
        return f"Booking({self.guest}, {self.guest}, {self.date}, {self.accepted})"

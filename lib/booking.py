class Booking:
    def __init__(self, id, date, available, space_id):
        self.id = id
        self.date = date
        self.available = available
        self.space_id = space_id

    # ensure two object with identical attrs will be found equal
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # return nicely formatted string version of peep object
    def __repr__(self):
        return f"Peep({self.id}, {self.message}, {self.date_created}, {self.user_id})"

    def book(self):
        pass

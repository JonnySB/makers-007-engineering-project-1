class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

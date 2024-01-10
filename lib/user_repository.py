from lib.user import User

class UserRepository():

    def __init__(self, connection):
        self.connection = connection
        
    def all(self):
        users = []
        rows = self.connection.execute("SELECT * FROM users")
        print(rows)
        for row in rows:
            user = User(row['id'], row["username"], row["email"])
            users.append(user)
        return users
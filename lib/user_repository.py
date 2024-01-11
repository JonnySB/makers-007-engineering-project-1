from lib.user import User
import bcrypt

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        users = []
        rows = self.connection.execute("SELECT * FROM users")

        for row in rows:
            user = User(row["id"], row["username"], row["email"], "None")
            users.append(user)
        return users

    def create(self, user):
        self.connection.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.hashed_password],
        )

    def find_user_id(self, user):
        rows = self.connection.execute(
            'SELECT * from users WHERE username = %s OR email = %s', [user, user])
        if len(rows) == 0:
            return False
        row = rows[0]
        return row['id']

    def verify_user_login(self, username, password):
        users_id = self.find_user_id(username)
        if not users_id:
            return False
        
        hashed_database_pw = self.connection.execute('SELECT hashed_password from users WHERE id = %s', [users_id])[0]['hashed_password']
        is_verified = bcrypt.checkpw(password.encode('utf-8'), hashed_database_pw)
        if not is_verified:
            return is_verified
        return users_id
    
    def get_user_details(self, user_id):
        rows = self.connection.execute("SELECT * FROM users WHERE id = %s", [user_id])[0]
        user = User(rows["id"], rows["username"], rows["email"], "None")
        return user

from lib.user import User
from lib.user_repository import UserRepository

def test_get_all_users (db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1, 'user1', 'user1@user.com', "Password"),
        User(2, 'user2', 'user2@user.com', "Password"),
        User(3, 'user3', 'user3@user.com', "Password"),
        User(4, 'user4', 'user4@user.com', "Password"),
        User(5, 'user5', 'user5@user.com', "Password")
    ]

def test_create_user (db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    user = User(None, 'user6', 'user6@user.com', 'Password')
    repository.create(user)
    users = repository.all()
    assert users == [
        User(1, 'user1', 'user1@user.com', "Password"),
        User(2, 'user2', 'user2@user.com', "Password"),
        User(3, 'user3', 'user3@user.com', "Password"),
        User(4, 'user4', 'user4@user.com', "Password"),
        User(5, 'user5', 'user5@user.com', "Password"),
        User(6, 'user6', 'user6@user.com', "Password"),
    ]
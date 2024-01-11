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

def test_find_user_invalid(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    # Finds user by username or email
    is_valid_user = repository.find_user_id('nasadk')
    assert is_valid_user == False

def test_find_user_by_username(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    # Finds user by username or email
    user_id = repository.find_user_id('user1')
    assert user_id == 1

def test_find_user_by_email(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    # Finds user by username or email
    is_valid_user = repository.find_user_id('user5@user.com')
    assert is_valid_user == 5

def test_correct_password(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    user = User(None, 'user6', 'user6@user.com', 'Password')

    repository.create(user)
    is_valid_password = repository.verify_user_login('user6', 'Password')
    assert is_valid_password == 6

def test_incorrect_password(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    user = User(None, 'user6', 'user6@user.com', 'Password')

    repository.create(user)
    is_valid_password = repository.verify_user_login('user6', 'dawdawd')
    assert is_valid_password == False


def test_get_single_user(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    user_details = repository.get_user_details(3)
    assert user_details == User(3, 'user3', 'user3@user.com', "Password")



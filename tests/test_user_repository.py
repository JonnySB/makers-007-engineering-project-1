from lib.user import User
from lib.user_repository import UserRepository

def test_get_all_users (db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1, 'user1', 'user1@user.com'),
        User(2, 'user2', 'user2@user.com'),
        User(3, 'user3', 'user3@user.com'),
        User(4, 'user4', 'user4@user.com'),
        User(5, 'user5', 'user5@user.com')
    ]
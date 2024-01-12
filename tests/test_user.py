import bcrypt

from lib.user import User

# Space constructs with an: id, name, description, price and user_id
def test_user_constructs():

    user = User(1, 'username', 'email', 'Password')
    assert user.id == 1
    assert user.username == 'username'
    assert user.email == 'email'
    #assert user.hashed_password == 'Password'
    assert bcrypt.checkpw("Password".encode("utf-8"), user.hashed_password)
    
    
#Format user to string
def test_user_format():

    user = User (1,'username','email', 'Password')
    assert str(user)== "User: 1, username, email"

# Compare two identical spaces
def test_identical_users():

    user1 = User(1, 'username', 'email', 'Password')
    user2 = User(1, 'username', 'email', 'Password')
    assert user1 == user2
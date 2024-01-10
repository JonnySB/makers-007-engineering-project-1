from lib.user import User

# Space constructs with an: id, name, description, price and user_id
def test_user_constructs():

    user = User(1, 'username', 'email')
    assert user.id == 1
    assert user.username == 'username'
    assert user.email == 'email'
    
    
#Format user to string
def test_user_format():

    user = User (1,'username','email')
    assert str(user)== "User: 1, username, email"

# Compare two identical spaces
def test_identical_users():

    user1 = User(1, 'username', 'email')
    user2 = User(1, 'username', 'email')
    assert user1 == user2
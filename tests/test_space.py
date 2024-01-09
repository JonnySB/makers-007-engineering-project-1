from lib.space import Space

# Space constructs with an: id, name, description, price and user_id
def test_space_constructs():

    space = Space(1, 'Test space', 'Test description', 100, 1)
    assert space.id == 1
    assert space.name == 'Test space'
    assert space.description == 'Test description'
    assert space.price == 100
    assert space.user_id == 1
    
# Format spaces to string
def test_space_format():

    space = Space(1, 'Test space', 'Test description', 100, 1)
    assert str(space) == "Space: 1, Test space, Test description, 100, 1"

# Compare two identical spaces
def test_identical_spaces():

    space1 = Space(1, 'Test space', 'Test description', 100, 1)
    space2 = Space(1, 'Test space', 'Test description', 100, 1)
    assert space1 == space2
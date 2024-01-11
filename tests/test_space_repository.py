from lib.space_repository import SpaceRepository
from lib.space import Space

'''
When I call #all,
I get all the spaces in the spaces table
'''
def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = SpaceRepository(db_connection)

    spaces = repository.all()
    assert spaces == [
        Space(1, 'Space1', 'Example description 1', 130, 1),
        Space(2, 'Space2', 'Example description 2', 130, 2),
        Space(3, 'Space3', 'Example description 3', 130, 3),
        Space(4, 'Space4', 'Example description 4', 130, 4),
        Space(5, 'Space5', 'Example description 5', 130, 1)
    ]

"""
When i call #find(id)
I get a specific space by the id
"""
def test_get_single_space(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = SpaceRepository(db_connection)

    space3 = repository.find(3)
    assert space3 == Space(3, 'Space3', 'Example description 3', 130, 3)

"""
When I call #create
I create a space in the spaces table
and can see it back in #all
"""
def test_create_space(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = SpaceRepository(db_connection)
    space = Space(None, 'Test Name', 'Test Description', 50.5, 5)
    repository.create(space)
    assert repository.all() == [
        Space(1, 'Space1', 'Example description 1', 130, 1),
        Space(2, 'Space2', 'Example description 2', 130, 2),
        Space(3, 'Space3', 'Example description 3', 130, 3),
        Space(4, 'Space4', 'Example description 4', 130, 4),
        Space(5, 'Space5', 'Example description 5', 130, 1),
        Space(6, 'Test Name', 'Test Description', 50.5, 5)
    ]
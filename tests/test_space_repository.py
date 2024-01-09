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
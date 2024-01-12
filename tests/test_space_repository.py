from lib.space_repository import SpaceRepository
from lib.space import Space

"""
When I call #all,
I get all the spaces in the spaces table
"""


def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()
    assert spaces == [
        Space(
            1,
            "Enchanted Retreat",
            "Discover the magic of this hidden gem. A cozy haven surrounded by nature, perfect for a peaceful escape.",
            130,
            1,
        ),
        Space(
            2,
            "Urban Oasis Loft",
            "Experience city living at its finest. Our modern loft offers stunning views and all the amenities you need for a stylish stay.",
            130,
            2,
        ),
        Space(
            3,
            "Sunset Serenity Cottage",
            "Unwind in our charming cottage with breathtaking sunset views. A tranquil setting for a memorable getaway.",
            130,
            3,
        ),
        Space(
            4,
            "Luxury Skyline Penthouse",
            "Indulge in luxury high above the city. Our penthouse boasts panoramic skyline views and top-notch amenities.",
            130,
            4,
        ),
        Space(
            5,
            "Seaside Bliss Villa",
            "Escape to paradise in our seaside villa. Relax to the sound of waves and enjoy the ultimate beachfront experience.",
            130,
            1,
        ),
    ]


"""
When i call #find(id)
I get a specific space by the id
"""


def test_get_single_space(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = SpaceRepository(db_connection)

    space3 = repository.find(3)
    assert space3 == Space(
        3,
        "Sunset Serenity Cottage",
        "Unwind in our charming cottage with breathtaking sunset views. A tranquil setting for a memorable getaway.",
        130,
        3,
    )


"""
When I call #create
I create a space in the spaces table
and can see it back in #all
"""


def test_create_space(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = SpaceRepository(db_connection)
    space = Space(None, "Test Name", "Test Description", 50.5, 5)
    repository.create(space)
    assert repository.all() == [
        Space(
            1,
            "Enchanted Retreat",
            "Discover the magic of this hidden gem. A cozy haven surrounded by nature, perfect for a peaceful escape.",
            130,
            1,
        ),
        Space(
            2,
            "Urban Oasis Loft",
            "Experience city living at its finest. Our modern loft offers stunning views and all the amenities you need for a stylish stay.",
            130,
            2,
        ),
        Space(
            3,
            "Sunset Serenity Cottage",
            "Unwind in our charming cottage with breathtaking sunset views. A tranquil setting for a memorable getaway.",
            130,
            3,
        ),
        Space(
            4,
            "Luxury Skyline Penthouse",
            "Indulge in luxury high above the city. Our penthouse boasts panoramic skyline views and top-notch amenities.",
            130,
            4,
        ),
        Space(
            5,
            "Seaside Bliss Villa",
            "Escape to paradise in our seaside villa. Relax to the sound of waves and enjoy the ultimate beachfront experience.",
            130,
            1,
        ),
        Space(6, "Test Name", "Test Description", 50.5, 5),
    ]

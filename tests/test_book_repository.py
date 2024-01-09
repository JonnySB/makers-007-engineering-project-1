from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new BookRepository

    books = repository.all() # Get all books

    # Assert on the results
    assert books == [
        Book(1, "Invisible Cities", "Italo Calvino"),
        Book(2, "The Man Who Was Thursday", "GK Chesterton"),
        Book(3, "Bluets", "Maggie Nelson"),
        Book(4, "No Place on Earth", "Christa Wolf"),
        Book(5, "Nevada", "Imogen Binnie"),
    ]

"""
When we call BookRepository#find
We get a single Book object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    book = repository.find(3)
    assert book == Book(3, "Bluets", "Maggie Nelson")

"""
When we call BookRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)

    created_book = repository.create(Book(None, "The Great Gatsby", "F. Scott Fitzgerald"))
    assert created_book == Book(6, "The Great Gatsby", "F. Scott Fitzgerald")

    result = repository.all()
    assert result == [
        Book(1, "Invisible Cities", "Italo Calvino"),
        Book(2, "The Man Who Was Thursday", "GK Chesterton"),
        Book(3, "Bluets", "Maggie Nelson"),
        Book(4, "No Place on Earth", "Christa Wolf"),
        Book(5, "Nevada", "Imogen Binnie"),
        Book(6, "The Great Gatsby", "F. Scott Fitzgerald"),
    ]

"""
When we call BookRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.delete(3) # Apologies to Maggie Nelson fans

    result = repository.all()
    assert result == [
        Book(1, "Invisible Cities", "Italo Calvino"),
        Book(2, "The Man Who Was Thursday", "GK Chesterton"),
        Book(4, "No Place on Earth", "Christa Wolf"),
        Book(5, "Nevada", "Imogen Binnie"),
    ]

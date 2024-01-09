from lib.book import Book

"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "Book(1, Test Title, Test Author)"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author")
    book2 = Book(1, "Test Title", "Test Author")
    assert book1 == book2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can assess a book for validity
"""
def test_book_validity():
    assert Book(1, "", "").is_valid() == False
    assert Book(1, "Title", "").is_valid() == False
    assert Book(1, "", "Author").is_valid() == False
    assert Book(1, "Title", None).is_valid() == False
    assert Book(1, None, "Author").is_valid() == False
    assert Book(1, "Title", "Author").is_valid() == True
    assert Book(None, "Title", "Author").is_valid() == True

"""
We can generate errors for an invalid book
"""
def test_book_errors():
    assert Book(1, "", "").generate_errors() == "Title can't be blank, Author name can't be blank"
    assert Book(1, "Title", "").generate_errors() == "Author name can't be blank"
    assert Book(1, "", "Author").generate_errors() == "Title can't be blank"
    assert Book(1, "Title", None).generate_errors() == "Author name can't be blank"
    assert Book(1, None, "Author").generate_errors() == "Title can't be blank"
    assert Book(1, "Title", "Author").generate_errors() == None
    assert Book(None, "Title", "Author").generate_errors() == None

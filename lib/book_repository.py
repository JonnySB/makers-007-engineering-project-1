from lib.book import Book


class BookRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
    
    def all_json(self):
        rows = self._connection.execute('SELECT * FROM books')

        return rows

    # Find a single book by its id
    def find(self, book_id):
        rows = self._connection.execute(
            'SELECT * from books WHERE id = %s', [book_id])
        row = rows[0]
        return Book(row["id"], row["title"], row["author_name"])

    # Create a new book
    def create(self, book):
        rows = self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s) RETURNING id', [
                                    book.title, book.author_name])
        row = rows[0]
        book.id = row["id"]
        return book

    # Delete a book by its id
    def delete(self, book_id):
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [book_id])
        return None

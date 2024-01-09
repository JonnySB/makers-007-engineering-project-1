from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import request, render_template, redirect, url_for

# You won't need to nest your routes in app.py in a method like this
def apply_example_routes(app):
    # GET /books
    # Returns a list of books
    @app.route('/books', methods=['GET'])
    def get_books():
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        books = repository.all()

        return render_template('books/index.html', books=books)

    @app.route('/api/books', methods=['GET'])
    def get_boots_api():
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)

        books = repository.all_json()
        return books

    # GET /books/<id>
    # Returns a single book
    @app.route('/books/<int:id>', methods=['GET'])
    def get_book(id):
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        book = repository.find(id)
        return render_template('books/show.html', book=book)


    # GET /books/new
    # Returns a form to create a new book
    @app.route('/books/new', methods=['GET'])
    def get_new_book():
        return render_template('books/new.html')


    # POST /books
    # Creates a new book
    @app.route('/books', methods=['POST'])
    def create_book():
        # Set up the database connection and repository
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)

        # Get the fields from the request form
        title = request.form['title']
        author_name = request.form['author_name']

        # Create a book object
        book = Book(None, title, author_name)

        # Check for validity and if not valid, show the form again with errors
        if not book.is_valid():
            return render_template('books/new.html', book=book, errors=book.generate_errors()), 400

        # Save the book to the database
        book = repository.create(book)

        # Redirect to the book's show route to the user can see it
        return redirect(f"/books/{book.id}")


    # POST /books/<id>/delete
    # Deletes a book
    @app.route('/books/<int:id>/delete', methods=['POST'])
    def delete_book(id):
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        repository.delete(id)

        # Typically we use the `url_for` function in Flask to generate URLs
        # rather than hand-writing them. `url_for` takes the name of the function
        # that generates the route and any arguments that are needed to generate
        # the URL.
        return redirect(url_for('get_books'))


from lib.database_connection import DatabaseConnection

# Run this file to reset your database using the seeds
# ; pipenv run python seed_dev_database.py

connection = DatabaseConnection(test_mode=False)
connection.connect()
connection.seed("seeds/book_store.sql")
# Add your own seed lines below...
# E.g.connection.seed("seeds/your_seed.sql")

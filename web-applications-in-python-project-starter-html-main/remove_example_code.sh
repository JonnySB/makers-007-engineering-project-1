#!/bin/sh

# Run this file to remove the example code from the project.
# ; ./remove_example_code.sh

echo "This will remove the example code from the project."
echo "DO NOT RUN THIS IF YOU HAVE ADDED YOUR OWN CODE."
echo "It may accidentally delete your code!"
echo "Continue? [y/N]"
read -r response
if [ "$response" != "y" ]; then
    echo "Aborting."
    exit 1
fi

rm lib/book_repository.py
rm lib/book.py
rm tests/test_book_repository.py
rm tests/test_book.py
rm tests/test_example_routes.py
rm example_routes.py
rm static/tdd-iceberg.png
rm static/what_is_this.md
rm seeds/book_store.sql
rm templates/emoji.html
rm templates/books/index.html
rm templates/books/new.html
rm templates/books/show.html
rmdir templates/books

grep -v book_store seed_dev_database.py > seed_dev_database.py.tmp
mv seed_dev_database.py.tmp seed_dev_database.py

sed -n -e '/== Example Code Below ==/{' -e ':a' -e 'N' -e '/== End Example Code ==\n/!ba' -e 's/.*//' -e '}' -e 'p' app.py > app.py.tmp
mv app.py.tmp app.py

sed -n -e '/== Example Code Below ==/{' -e ':a' -e 'N' -e '/== End Example Code ==\n/!ba' -e 's/.*//' -e '}' -e 'p' tests/test_app.py > tests/test_app.py.tmp
mv tests/test_app.py.tmp tests/test_app.py

rm remove_example_code.sh

echo "Completed."

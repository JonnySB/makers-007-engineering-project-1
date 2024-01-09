## 1. Design and create the Table
## 2. Create Test SQL seeds

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)
class Space


# Repository class
# (in lib/student_repository.py)
class SpaceRepository
```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Space:
    def __init__(self, id, name, description, price, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space: {self.id}, {self.name}, {self.description}, {self.price}, {self.user_id}"

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'
```

_You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed._

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class SpaceRepository():

    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, name, description, price, user_id FROM spaces;

        # Returns an array of Space objects.



```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = SpaceRepository()

spaces = repo.all()

len(spaces) # =>  5

spaces[0].id # =>  1
spaces[0].name # =>  'Space1'
spaces[0].description # =>  'Example description 1'
spaces[0].price # 130
spaces[0].user_id # 1

```

Encode this example as a test.

## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

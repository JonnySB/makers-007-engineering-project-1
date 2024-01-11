from lib.space import Space

class SpaceRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(row['id'], row['name'], row['description'], row['price'], row['user_id'])
            spaces.append(space)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces where id=%s', [id])
        row = rows[0]
        return Space(row['id'], row['name'], row['description'], row['price'], row['user_id'])
    
    def create(self, space):
        rows = self._connection.execute(
            'INSERT INTO spaces (name, description, price, user_id) VALUES (%s, %s, %s, %s) RETURNING id', 
            [space.name, space.description, space.price, space.user_id]
        )
        row = rows[0]
        space.id = row["id"]
        return space
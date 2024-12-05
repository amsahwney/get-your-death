from . import CONN, CURSOR

class User:
    def __init__(self, first_name:str, last_name:str, age:int=None, id:int=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name} )"
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL, 
        age INTEGER
        )
        """
        CONN.execute(sql)

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM users
        """

        user_data = CURSOR.execute(sql).fetchall()

        user_instances = [User(
            id=u[0],
            first_name=u[1],
            last_name=u[2],
            age=u[3]
        ) for u in user_data ]

        return user_instances
    
# CRUD METHODS
    def create(self):
        sql = """
        INSERT INTO users (first_name, last_name, age)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age])
        CONN.commit()

        last_row_sql = """
        SELECT id FROM users
        ORDER BY id DESC
        LIMIT 1
        """

        self.id = CURSOR.execute(last_row_sql).fetchone()[0]

        return self
 
    def update(self):
        sql = """
        UPDATE users
        SET first_name = ?, last_name = ?, age = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.first_name, self.last_name, self.age, self.id])
        CONN.commit()

        return self

    def save(self):
        if self.id:
            self.update()
        else:
            self.create()
        return self
    
    def destroy(self):
        sql = """
        DELETE FROM users
        where id = ?
        """

        CURSOR.execute(sql, [self.id])
        CONN.commit()

        self.id = None

#JOIN METHODS
    # def reviews(self):
    #     sql = """
    #     SELECT * FROM reviews
    #     WHERE book_id = ?
    #     """

    #     review_tuples = CURSOR.execute(sql, [self.id]).fetchall()

    #     review_instances = [ Review(
    #         id=rv[0], 
    #         stars=rv[1], 
    #         username=rv[2], 
    #         book_id=rv[3]
    #     ) for rv in review_tuples ]

    #     return review_instances


class Directive:
    pass 
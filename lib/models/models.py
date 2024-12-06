from . import CONN, CURSOR

class User:
    def __init__(self, first_name:str, last_name:str, age:int=None, email:str=None, phone_number:int=None, id:int=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name} )"
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL, 
        age INTEGER,
        email TEXT,
        phone_number INTEGER
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
            age=u[3],
            email=u[4],
            phone_number=u[5]
        ) for u in user_data ]

        return user_instances
    
#for debugging purposes
    @classmethod
    def drop_table(cls):
        sql = f"DROP TABLE IF EXISTS users"
        CONN.execute(sql)
        CONN.commit()
    
# CRUD METHODS
    def create(self):
        sql = """
        INSERT INTO users (first_name, last_name, age, email, phone_number)
        VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age, self.email, self.phone_number])
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
        SET first_name = ?, last_name = ?, age = ?, email = ?, phone_number = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.first_name, self.last_name, self.age, self.email, self.phone_number, self.id])
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

#JOIN METHODS USER CLASS
    def directives(self):
        sql = """
        SELECT * FROM directives
        WHERE directive_owner = ?
        """

        directive_tuples = CURSOR.execute(sql, [self.id]).fetchall()

        directive_instances = [ Directive(
            id=d[0], 
            location=d[1], 
            directive_owner=d[2], 
            proxy=d[3]
        ) for d in directive_tuples ]

        return directive_instances


class Directive:
    def __init__(self, location:str, directive_owner:int, proxy:int, id:int=None):
        self.id = id
        self.location = location
        self.directive_owner = directive_owner
        self.proxy = proxy

    def __repr__(self):
        return f'Directive(id={self.id}, directive_owner={self.directive_owner})' 

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS directives (
        id INTEGER PRIMARY KEY,
        location TEXT,
        directive_owner INTEGER,
        proxy INTEGER
        ) 
        """ 

        CONN.execute(sql)

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM directives
        """

        directive_data = CURSOR.execute(sql).fetchall()

        directive_instances = [ Directive(
            id=d[0],
            location=d[1],
            directive_owner=d[2],
            proxy=d[3]
        ) for d in directive_data ] 
        return directive_instances

    def create(self):
        sql = """
        INSERT INTO directives (location, directive_owner, proxy)
        VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, [self.location, self.directive_owner, self.proxy])
        CONN.commit()

        last_row_sql = """
        SELECT id FROM directives
        ORDER by id DESC
        LIMIT 1
        """

        self.id = CURSOR.execute(last_row_sql).fetchone()[0]
        return self
    
    def update(self):
        sql = """
        UPDATE directives
        SET location = ?, directive_owner = ?, proxy = ?
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.location, self.directive_owner, self.proxy, self.id])
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
        DELETE FROM directives
        WHERE id = ?
        """

        CURSOR.execute(sql, [self.id])
        CONN.commit()
        self.id = None

# JOIN METHODS DIRECTIVE CLASS 
    def user(self):
        return User.get_by_id(self.directive_owner)

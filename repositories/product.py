import psycopg2


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS product (
    id SERIAL UNIQUE,
    description VARCHAR(150) NOT NULL,
    org VARCHAR(150) NOT NULL
)
"""

class ProductRepository:
    def __init__(self, db_conn):
        self.__conn = db_conn
        self.__init_tables()

    def __init_tables(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(CREATE_TABLE)
            self.__conn.commit()
            cursor.close()
        except psycopg2.DatabaseError:
            self.__conn.rollback()
            return

    def insert_row(self, product):
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO product (description, org)
            VALUES (%s, %s)
            RETURNING id;
            """,
            ["test", "test"]
        )
        self.__conn.commit()
        _id = cursor.fetchone()[0]
        cursor.close()
        return _id

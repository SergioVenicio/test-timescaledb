import psycopg2


CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS timeline (
    time TIMESTAMPTZ NOT NULL,
    product_id INTEGER NOT NULL,
    action VARCHAR(250) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
)
"""

CREATE_HYPERTABLE = """
SELECT create_hypertable('timeline', 'time')
"""


class TimelineRepository:
    def __init__(self, db_conn):
        self.__conn = db_conn
        self.__init_tables()

    def __init_tables(self):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(CREATE_TABLE)
            cursor.execute(CREATE_HYPERTABLE)
            self.__conn.commit()
        except psycopg2.DatabaseError:
            self.__conn.rollback()
            return

    def insert_row(self, timeline):
        cursor = self.__conn.cursor()
        cursor.execute("""
            INSERT INTO timeline (product_id, time, action)
            VALUES (%s, %s, %s);
        """, (timeline.product_id, timeline.time, timeline.action))
        self.__conn.commit()
        cursor.close()
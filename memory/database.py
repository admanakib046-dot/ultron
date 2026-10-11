import sqlite3


class MemoryDatabase:

    def __init__(self, db_name="memory/ultron.db"):

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT,

            category TEXT,

            importance INTEGER,

            created TEXT,

            updated TEXT,

            last_used TEXT

        )
        """)

        self.conn.commit()

    def save_memory(self, key, value,
                    category,
                    importance,
                    created,
                    updated,
                    last_used):

        self.cursor.execute("""

        INSERT OR REPLACE INTO memories
        (key,value,category,importance,created,updated,last_used)

        VALUES (?,?,?,?,?,?,?)

        """, (

            key,
            value,
            category,
            importance,
            created,
            updated,
            last_used

        ))

        self.conn.commit()

    def get_memory(self, key):

        self.cursor.execute(

            "SELECT * FROM memories WHERE key=?",
            (key,)

        )

        return self.cursor.fetchone()

    def delete_memory(self, key):

        self.cursor.execute(

            "DELETE FROM memories WHERE key=?",
            (key,)

        )

        self.conn.commit()

    def search(self, keyword):

        self.cursor.execute(

            """

            SELECT * FROM memories

            WHERE key LIKE ?

            OR value LIKE ?

            """,

            (f"%{keyword}%", f"%{keyword}%")

        )

        return self.cursor.fetchall()

    def all(self):

        self.cursor.execute(

            "SELECT * FROM memories"

        )

        return self.cursor.fetchall()

    def close(self):

        self.conn.close()
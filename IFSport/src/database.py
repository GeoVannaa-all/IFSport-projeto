import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            "sistema_esportivo.db",
            check_same_thread=False
        )
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

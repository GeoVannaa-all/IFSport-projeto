import sqlite3
from datetime import date

class Database:
    def __init__(self, db_name="sistema_esportivo.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def create_tables(self):
        # Cria tabela de alunos completa
        self.execute("""
        CREATE TABLE IF NOT EXISTS Aluno (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            data_nascimento TEXT,
            matricula TEXT,
            curso TEXT,
            data_cadastro TEXT
        )
        """)

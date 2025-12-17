import sqlite3

class Database:
    def __init__(self, nome_banco="sistema_esportivo.db"):
        self.nome_banco = nome_banco

    def conectar(self):
        return sqlite3.connect(self.nome_banco)

    def criar_tabelas(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Aluno (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            senha TEXT,
            curso TEXT
        );
        """)

        conn.commit()
        conn.close()

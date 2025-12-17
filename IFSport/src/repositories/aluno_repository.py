import sqlite3
from models.aluno import Aluno

class AlunoRepository:
    def __init__(self, nome_banco="sistema_esportivo.db"):
        self.nome_banco = nome_banco

    def salvar(self, aluno: Aluno):
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Aluno (nome, email, senha, curso)
        VALUES (?, ?, ?, ?)
        """, (aluno.nome, aluno.email, aluno.senha, aluno.curso))

        conn.commit()
        conn.close()

    def listar(self):
        conn = sqlite3.connect(self.nome_banco)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Aluno")
        registros = cursor.fetchall()

        alunos = []
        for r in registros:
            alunos.append(Aluno(r[1], r[2], r[3], r[4], r[0]))

        conn.close()
        return alunos

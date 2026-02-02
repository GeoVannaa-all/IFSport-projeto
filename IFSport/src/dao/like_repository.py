from database.database import Database

class LikeRepository:
    def __init__(self, db: Database):
        self.db = db

    def adicionar(self, id_postagem, id_aluno):
        sql = "INSERT OR IGNORE INTO Curtida (id_postagem, id_aluno) VALUES (?, ?)"
        self.db.execute(sql, (id_postagem, id_aluno))

    def remover(self, id_postagem, id_aluno):
        sql = "DELETE FROM Curtida WHERE id_postagem = ? AND id_aluno = ?"
        self.db.execute(sql, (id_postagem, id_aluno))

    def contar(self, id_postagem):
        sql = "SELECT COUNT(*) FROM Curtida WHERE id_postagem = ?"
        # AGORA: Pegamos o cursor retornado pelo execute
        cursor = self.db.execute(sql, (id_postagem,))
        # E chamamos fetchone() no cursor
        resultado = cursor.fetchone()
        return resultado[0] if resultado else 0

    def usuario_curtiu(self, id_postagem, id_aluno):
        sql = "SELECT 1 FROM Curtida WHERE id_postagem = ? AND id_aluno = ?"
        cursor = self.db.execute(sql, (id_postagem, id_aluno))
        return cursor.fetchone() is not None
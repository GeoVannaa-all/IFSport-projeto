class LikeRepository:
    def __init__(self, db):
        self.db = db

    def curtir(self, id_postagem, id_aluno):
        self.db.execute("""
            INSERT INTO Curtida (id_postagem, id_aluno)
            VALUES (?, ?)
        """, (id_postagem, id_aluno))

    def contar(self, id_postagem):
        self.db.execute("""
            SELECT COUNT(*) FROM Curtida WHERE id_postagem = ?
        """, (id_postagem,))
        return self.db.fetchone()[0]

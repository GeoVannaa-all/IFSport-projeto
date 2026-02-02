class LikeRepository:
    def __init__(self, db):
        self.db = db

    def curtir(self, id_aluno, id_postagem):
        self.db.execute("""
            INSERT OR IGNORE INTO Curtida (id_aluno, id_postagem)
            VALUES (?, ?)
        """, (id_aluno, id_postagem))

    def remover(self, id_aluno, id_postagem):
        self.db.execute("""
            DELETE FROM Curtida
            WHERE id_aluno = ? AND id_postagem = ?
        """, (id_aluno, id_postagem))

    def contar(self, id_postagem):
        self.db.execute("""
            SELECT COUNT(*) FROM Curtida
            WHERE id_postagem = ?
        """, (id_postagem,))
        resultado = self.db.fetchone()
        return resultado[0] if resultado else 0

    # MÉTODO BASE
    def verificar(self, id_aluno, id_postagem):
        self.db.execute("""
            SELECT 1 FROM Curtida
            WHERE id_aluno = ? AND id_postagem = ?
        """, (id_aluno, id_postagem))
        return self.db.fetchone() is not None

   
    def usuario_curtiu(self, id_postagem, id_aluno):
        return self.verificar(id_aluno, id_postagem)

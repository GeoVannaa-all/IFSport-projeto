class ComentarioRepository:
    def __init__(self, db):
        self.db = db

    def criar(self, texto, id_postagem, id_aluno):
        self.db.execute("""
            INSERT INTO Comentario (texto, data_comentario, id_postagem, id_aluno)
            VALUES (?, datetime('now'), ?, ?)
        """, (texto, id_postagem, id_aluno))

    def listar(self, id_postagem):
        self.db.execute("""
            SELECT texto FROM Comentario WHERE id_postagem = ?
        """, (id_postagem,))
        return self.db.fetchall()

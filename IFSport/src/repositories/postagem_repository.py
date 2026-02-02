class PostagemRepository:
    def __init__(self, db):
        self.db = db

    def criar(self, titulo, conteudo, imagem, id_servidor):
        self.db.execute("""
            INSERT INTO Postagem (titulo, conteudo, imagem, data_postagem, id_servidor)
            VALUES (?, ?, ?, datetime('now'), ?)
        """, (titulo, conteudo, imagem, id_servidor))

    def listar(self):
        self.db.execute("""
            SELECT 
                p.id_postagem,
                p.titulo,
                p.conteudo,
                p.imagem,
                p.data_postagem,
                (SELECT COUNT(*) FROM Curtida c WHERE c.id_postagem = p.id_postagem) AS curtidas
            FROM Postagem p
            ORDER BY p.data_postagem DESC
        """)
        return self.db.fetchall()

    def excluir(self, id_postagem):
        self.db.execute("DELETE FROM Curtida WHERE id_postagem = ?", (id_postagem,))
        self.db.execute("DELETE FROM Comentario WHERE id_postagem = ?", (id_postagem,))
        self.db.execute("DELETE FROM Postagem WHERE id_postagem = ?", (id_postagem,))

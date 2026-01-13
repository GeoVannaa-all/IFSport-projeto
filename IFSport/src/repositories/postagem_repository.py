class PostagemRepository:
    def __init__(self, db):
        self.db = db

    def criar(self, titulo, conteudo, imagem, id_servidor):
        self.db.execute("""
            INSERT INTO Postagem (titulo, conteudo, imagem, data_postagem, id_servidor)
            VALUES (?, ?, ?, datetime('now'), ?)
        """, (titulo, conteudo, imagem, id_servidor))

    def listar(self):
        self.db.execute("SELECT * FROM Postagem ORDER BY data_postagem DESC")
        return self.db.fetchall()

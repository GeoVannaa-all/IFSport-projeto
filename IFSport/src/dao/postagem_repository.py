from database.database import Database
from datetime import datetime

class PostagemRepository:
    def __init__(self, db: Database):
        self.db = db

    def criar(self, titulo, conteudo, imagem, id_servidor):
        sql = """
            INSERT INTO Postagem (titulo, conteudo, imagem, data_postagem, id_servidor)
            VALUES (?, ?, ?, ?, ?)
        """
        # Usa o seu método 'execute' padrão
        self.db.execute(sql, (
            titulo, 
            conteudo, 
            imagem, 
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            id_servidor
        ))

    def listar(self):
        sql = """
            SELECT 
                p.id_postagem,
                p.titulo,
                p.conteudo,
                p.imagem,
                p.data_postagem,
                (SELECT COUNT(*) FROM Curtida c WHERE c.id_postagem = p.id_postagem) AS curtidas
            FROM Postagem p
            ORDER BY p.data_postagem DESC
        """
        # 1. Executa a query
        cursor = self.db.execute(sql)
        
        # 2. Extrai os dados da lista usando fetchall()
        return cursor.fetchall()

    def excluir(self, id_postagem):
        # Remove dependências e a postagem usando 'execute'
        self.db.execute("DELETE FROM Curtida WHERE id_postagem = ?", (id_postagem,))
        self.db.execute("DELETE FROM Comentario WHERE id_postagem = ?", (id_postagem,))
        self.db.execute("DELETE FROM Postagem WHERE id_postagem = ?", (id_postagem,))
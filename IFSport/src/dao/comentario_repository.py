from database.database import Database
from datetime import datetime

class ComentarioRepository:
    def __init__(self, db: Database):
        self.db = db

    def adicionar(self, id_aluno, id_postagem, texto):
        """Salva um novo comentário no banco."""
        sql = """
            INSERT INTO Comentario (texto, data_comentario, id_aluno, id_postagem)
            VALUES (?, ?, ?, ?)
        """
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.db.execute(sql, (texto, data_hora, id_aluno, id_postagem))
        self.db.commit()

    def listar_por_postagem(self, id_postagem):
        """
        Retorna: [(nome_aluno, texto, data), ...]
        Faz um JOIN com a tabela Aluno para pegar o nome de quem comentou.
        """
        sql = """
            SELECT a.nome, c.texto, c.data_comentario
            FROM Comentario c
            JOIN Aluno a ON c.id_aluno = a.id_aluno
            WHERE c.id_postagem = ?
            ORDER BY c.id_comentario ASC
        """
        cursor = self.db.execute(sql, (id_postagem,))
        return cursor.fetchall()

    def contar(self, id_postagem):
        """Conta quantos comentários um post tem."""
        sql = "SELECT COUNT(*) FROM Comentario WHERE id_postagem = ?"
        cursor = self.db.execute(sql, (id_postagem,))
        return cursor.fetchone()[0]
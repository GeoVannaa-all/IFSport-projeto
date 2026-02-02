from datetime import date

class NotificacaoRepository:
    def __init__(self, db):
        self.db = db

    def criar(self, mensagem, id_aluno=None, id_servidor=None):
        self.db.execute("""
            INSERT INTO Notificacao (mensagem, data_envio, lida, id_aluno, id_servidor)
            VALUES (?, ?, 0, ?, ?)
        """, (
            mensagem,
            date.today().isoformat(),
            id_aluno,
            id_servidor
        ))

    def listar_por_aluno(self, id_aluno):
        cursor = self.db.execute("""
            SELECT id_notificacao, mensagem, data_envio, lida
            FROM Notificacao
            WHERE id_aluno = ?
            ORDER BY data_envio DESC
        """, (id_aluno,))
        return cursor.fetchall()

    def marcar_como_lida(self, id_notificacao):
        self.db.execute("""
            UPDATE Notificacao SET lida = 1
            WHERE id_notificacao = ?
        """, (id_notificacao,))

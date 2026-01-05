from repositories.database import Database
from models.aluno import Aluno

class AlunoRepository:
    def __init__(self, db: Database):
        self.db = db

    def validar_login(self, email, senha):
        query = "SELECT * FROM Aluno WHERE email = %s AND senha = %s"
        self.db.query(query, (email, senha))
        aluno_data = self.db.fetchone()
        if aluno_data:
            return Aluno(*aluno_data)
        return None

    def inscrever_aluno_evento(self, aluno_id, modalidade_id):
        query = "INSERT INTO Inscricao (id_aluno, id_modalidade, data_inscricao, status) VALUES (%s, %s, NOW(), 'Pendente')"
        try:
            self.db.query(query, (aluno_id, modalidade_id))
            return True
        except Exception as e:
            print(e)
            return False

    def get_notificacoes(self, aluno_id):
        query = "SELECT * FROM Notificacao WHERE id_aluno = %s"
        self.db.query(query, (aluno_id,))
        notificacoes_data = self.db.fetchall()
        return [Notificacao(*n) for n in notificacoes_data]

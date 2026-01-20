class InscricaoRepository:
    def __init__(self, db):
        self.db = db

    def criar(self, aluno_id, modalidade_id):
        self.db.execute(
            "INSERT INTO inscricao VALUES (NULL, ?, ?, 'Pendente')",
            (aluno_id, modalidade_id)
        )

    def listar_pendentes(self):
        return self.db.fetchall("""
            SELECT i.id, a.nome, m.nome
            FROM inscricao i
            JOIN aluno a ON a.id = i.aluno_id
            JOIN modalidade m ON m.id = i.modalidade_id
            WHERE i.status = 'Pendente'
        """)

    def aprovar(self, inscricao_id):
        self.db.execute(
            "UPDATE inscricao SET status = 'Aprovado' WHERE id = ?",
            (inscricao_id,)
        )

#comunicação com o banco de dados. (DAO)
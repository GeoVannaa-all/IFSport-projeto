class InscricaoRepository:
    def __init__(self, db):
        self.db = db

    def solicitar(self, id_aluno, id_modalidade):
        self.db.execute("""
            INSERT INTO Inscricao (data_inscricao, status, id_aluno, id_modalidade)
            VALUES (date('now'), 'PENDENTE', ?, ?)
        """, (id_aluno, id_modalidade))

    def listar_pendentes(self):
        cursor = self.db.execute("""
            SELECT 
                i.id_inscricao,
                a.nome,
                a.matricula,
                m.nome,
                m.id_modalidade
            FROM Inscricao i
            JOIN Aluno a ON a.id_aluno = i.id_aluno
            JOIN Modalidade m ON m.id_modalidade = i.id_modalidade
            WHERE i.status = 'PENDENTE'
              AND m.status = 'ATIVA'
        """)
        return cursor.fetchall()

    def aprovar(self, id_inscricao):
        self.db.execute("""
            UPDATE Inscricao
            SET status = 'APROVADO'
            WHERE id_inscricao = ?
        """, (id_inscricao,))

    def recusar(self, id_inscricao):
        self.db.execute("""
            UPDATE Inscricao
            SET status = 'RECUSADO'
            WHERE id_inscricao = ?
        """, (id_inscricao,))

    def buscar_por_aluno(self, id_aluno):
        cursor = self.db.execute("""
            SELECT m.nome, i.status
            FROM Inscricao i
            JOIN Modalidade m ON m.id_modalidade = i.id_modalidade
            WHERE i.id_aluno = ?
        """, (id_aluno,))
        return cursor.fetchall()

    def listar_aprovados_por_modalidade(self, id_modalidade):
        cursor = self.db.execute("""
            SELECT a.nome, a.matricula
            FROM Inscricao i
            JOIN Aluno a ON a.id_aluno = i.id_aluno
            WHERE i.id_modalidade = ?
              AND i.status = 'APROVADO'
        """, (id_modalidade,))
        return cursor.fetchall()

    def contar_aprovados(self, id_modalidade):
        cursor = self.db.execute("""
            SELECT COUNT(*)
            FROM Inscricao
            WHERE id_modalidade = ?
              AND status = 'APROVADO'
        """, (id_modalidade,))
        return cursor.fetchone()[0]

    def remover_pendentes_da_modalidade(self, id_modalidade):
        self.db.execute("""
            DELETE FROM Inscricao
            WHERE id_modalidade = ?
              AND status = 'PENDENTE'
        """, (id_modalidade,))

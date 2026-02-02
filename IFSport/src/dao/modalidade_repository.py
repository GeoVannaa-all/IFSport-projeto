from database.database import Database

class ModalidadeRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_disponiveis(self):
        # Retorna apenas modalidades com vagas > 0
        sql = "SELECT id_modalidade, nome, vagas FROM Modalidade WHERE vagas > 0"
        cursor = self.db.execute(sql)
        return cursor.fetchall()
    
    def criar(self, nome, vagas):
        self.db.execute("""
            INSERT INTO Modalidade (nome, descricao, vagas, status)
            VALUES (?, '', ?, 'ATIVA')
        """, (nome, vagas))

    def listar_disponiveis(self):
        cursor = self.db.execute("""
            SELECT id_modalidade, nome, vagas
            FROM Modalidade
            WHERE status = 'ATIVA'
        """)
        return cursor.fetchall()

    def listar_todas(self):
        cursor = self.db.execute("""
            SELECT id_modalidade, nome, vagas
            FROM Modalidade
        """)
        return cursor.fetchall()

    def buscar_vagas(self, id_modalidade):
        cursor = self.db.execute("""
            SELECT vagas FROM Modalidade
            WHERE id_modalidade = ?
        """, (id_modalidade,))
        return cursor.fetchone()[0]

    def encerrar(self, id_modalidade):
        self.db.execute("""
            UPDATE Modalidade
            SET status = 'ENCERRADA'
            WHERE id_modalidade = ?
        """, (id_modalidade,))

    def excluir(self, id_modalidade):
        self.db.execute("""
            DELETE FROM Inscricao WHERE id_modalidade = ?
        """, (id_modalidade,))

        self.db.execute("""
            DELETE FROM Modalidade WHERE id_modalidade = ?
        """, (id_modalidade,))

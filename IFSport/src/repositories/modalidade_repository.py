from repositories.database import Database
from models.modalidade import Modalidade

class ModalidadeRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_modalidades(self):
        query = "SELECT * FROM Modalidade"
        self.db.query(query)
        modalidades_data = self.db.fetchall()
        return [Modalidade(*m) for m in modalidades_data]

from repositories.database import Database
from models.modalidade import Modalidade

class ModalidadeRepository:
    def __init__(self, db):
        self.db = db

    def listar(self):
        return self.db.fetchall("SELECT * FROM modalidade")

    def reduzir_vaga(self, modalidade_id):
        self.db.execute(
            "UPDATE modalidade SET vagas = vagas - 1 WHERE id = ? AND vagas > 0",
            (modalidade_id,)
        )

#comunicação com o banco de dados. (DAO)
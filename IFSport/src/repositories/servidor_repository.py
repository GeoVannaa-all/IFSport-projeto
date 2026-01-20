from .database import Database

class ServidorRepository:
    def __init__(self):
        self.admin_password = "1234"

    def login_admin(self, senha):
        return senha == self.admin_password

#comunicação com o banco de dados. (DAO)
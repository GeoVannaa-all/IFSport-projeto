from .database import Database
#Admin não precisa de tabela
class ServidorRepository:
    def __init__(self):
        self.admin_password = "1234"

    def login_admin(self, senha):
        return senha == self.admin_password


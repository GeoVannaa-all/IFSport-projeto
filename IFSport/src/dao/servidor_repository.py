from database.database import Database

class ServidorRepository:
    # 1. Adicione o parâmetro 'db' aqui no init
    def __init__(self, db):
        self.db = db  # 2. Guarde o banco na classe (mesmo que não use agora)
        self.admin_password = "1234"

    def login_admin(self, senha):
        # Por enquanto é fixo, mas futuramente você poderá usar 
        # self.db para buscar a senha real no banco
        return senha == self.admin_password
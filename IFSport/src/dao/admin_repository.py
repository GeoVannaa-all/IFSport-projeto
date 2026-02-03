from database.database import Database
from datetime import date

class AdminRepository:
    def __init__(self, db: Database):
        self.db = db

    def login_admin(self, email, senha):
        """
        Verifica as credenciais na tabela Servidor.
        Retorna uma tupla (id_servidor, nome, cargo) se o login for válido.
        Retorna None se falhar.
        """
        sql = """
            SELECT id_servidor, nome, cargo 
            FROM Servidor 
            WHERE email = ? AND senha = ?
        """
        cursor = self.db.execute(sql, (email, senha))
        return cursor.fetchone()

    def buscar_por_id(self, id_servidor):
        """
        Busca os dados completos de um admin pelo ID.
        Útil para carregar perfil no dashboard.
        """
        sql = """
            SELECT id_servidor, nome, email, cargo, data_cadastro
            FROM Servidor 
            WHERE id_servidor = ?
        """
        cursor = self.db.execute(sql, (id_servidor,))
        return cursor.fetchone()

    def criar_admin(self, nome, email, senha, cargo):
        """
        Cria um novo servidor/admin manualmente (caso precise criar via código).
        """
        sql = """
            INSERT INTO Servidor (nome, email, senha, cargo, data_cadastro)
            VALUES (?, ?, ?, ?, ?)
        """
        data_atual = date.today().isoformat()
        self.db.execute(sql, (nome, email, senha, cargo, data_atual))
        self.db.commit()

    def existe_admin(self):
        """
        Verifica se existe pelo menos um admin cadastrado.
        Útil para inicialização do sistema.
        """
        sql = "SELECT COUNT(*) FROM Servidor"
        cursor = self.db.execute(sql)
        count = cursor.fetchone()[0]
        return count > 0
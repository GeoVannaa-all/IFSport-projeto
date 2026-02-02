from database.database import Database
from models.aluno import Aluno
from datetime import date

class AlunoRepository:
    def __init__(self, db: Database):
        self.db = db

    # CADASTRO
    def cadastrar(self, nome, email, senha, data_nascimento, matricula, curso):
        sql = """
        INSERT INTO Aluno 
        (nome, email, senha, data_nascimento, matricula, curso, data_cadastro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute(sql, (
            nome,
            email,
            senha,
            data_nascimento,
            matricula,
            curso,
            date.today().isoformat()
        ))

    # LOGIN
    def login_aluno(self, email, senha):
        sql = "SELECT * FROM Aluno WHERE email = ? AND senha = ?"
        cursor = self.db.execute(sql, (email, senha))
        aluno_data = cursor.fetchone()

        if aluno_data:
            return Aluno(*aluno_data)
        return None

    # LISTAR TODOS
    def listar(self):
        sql = "SELECT * FROM Aluno"
        cursor = self.db.execute(sql)
        alunos_data = cursor.fetchall()
        return [Aluno(*a) for a in alunos_data]

    # ATUALIZAR
    def atualizar(self, aluno: Aluno):
        sql = """
        UPDATE Aluno
        SET nome = ?, email = ?, senha = ?, data_nascimento = ?, matricula = ?, curso = ?
        WHERE id_aluno = ?
        """
        self.db.execute(sql, (
            aluno.nome,
            aluno.email,
            aluno.senha,
            aluno.data_nascimento,
            aluno.matricula,
            aluno.curso,
            aluno.id_aluno
        ))


    def excluir(self, id_aluno):
        sql = "DELETE FROM Aluno WHERE id_aluno = ?"
        self.db.execute(sql, (id_aluno,))

   
    def buscar_por_id(self, id_aluno):
       
        query = """
            SELECT nome, email, matricula, curso 
            FROM Aluno 
            WHERE id_aluno = ?
        """
        
       
        cursor = self.db.execute(query, (id_aluno,))
        
       
        dados = cursor.fetchone()
        
        return dados 
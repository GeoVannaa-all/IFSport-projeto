class Aluno:
    def __init__(self, nome, email, senha, curso, id_aluno=None):
        self.id_aluno = id_aluno
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curso = curso

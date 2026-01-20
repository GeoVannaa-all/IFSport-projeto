class Aluno:
    def __init__(self, id_aluno, nome, email, senha, data_nascimento, matricula, curso, data_cadastro):
        self.__id_aluno = id_aluno
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__data_nascimento = data_nascimento
        self.__matricula = matricula
        self.__curso = curso
        self.__data_cadastro = data_cadastro


    def get_id_aluno(self):
        return self.__id_aluno
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_matricula(self):
        return self.__matricula
    def get_curso(self):
        return self.__curso
    def get_data_cadastro(self):
        return self.__data_cadastro
    
    def set_id_aluno(self, id_aluno):
        self.__id_aluno = id_aluno
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_senha(self, senha):
        self.__senha = senha
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def set_curso(self, curso):
        self.__curso = curso
    def set_data_cadastro(self, data_cadastro):
        self.__data_cadastro = data_cadastro

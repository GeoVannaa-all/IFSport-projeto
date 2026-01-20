from datetime import date, datetime

class Aluno:
    def __init__(self, id_aluno, nome, email, senha,data_nascimento, matricula, curso, data_cadastro):
        self.__id_aluno = id_aluno
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.matricula = matricula
        self.curso = curso

        if isinstance(data_cadastro, str):
            data_cadastro = datetime.strptime(data_cadastro, "%Y-%m-%d").date()
        self.__data_cadastro = data_cadastro

    @property
    def id_aluno(self):
        return self.__id_aluno

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome or len(nome) < 3:
            raise ValueError("Nome inválido")
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if "@" not in email:
            raise ValueError("Email inválido")
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if len(senha) < 3:
            raise ValueError("Senha muito curta")
        self.__senha = senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str):
            data = datetime.strptime(data, "%Y-%m-%d").date()

        if data >= date.today():
            raise ValueError("Data inválida")

        self.__data_nascimento = data

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if not matricula:
            raise ValueError("Matrícula obrigatória")
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        if not curso:
            raise ValueError("Curso obrigatório")
        self.__curso = curso

    @property
    def data_cadastro(self):
        return self.__data_cadastro

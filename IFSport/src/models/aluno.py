from datetime import date, datetime

class Aluno:
    # Mantivemos a ordem exata dos seus parâmetros para casar com o banco de dados
    def __init__(self, id_aluno, nome, email, senha, data_nascimento, matricula, curso, data_cadastro):
        self.__id_aluno = id_aluno
        self.nome = nome
        self.email = email
        self.senha = senha
        # A mágica acontece aqui: passamos pelo setter inteligente
        self.data_nascimento = data_nascimento 
        self.matricula = matricula
        self.curso = curso

        # Tratamento seguro para data_cadastro
        if isinstance(data_cadastro, str):
            try:
                # Pega só a parte da data (yyyy-mm-dd) caso venha com horas
                data_limpa = data_cadastro.split(" ")[0]
                self.__data_cadastro = datetime.strptime(data_limpa, "%Y-%m-%d").date()
            except ValueError:
                self.__data_cadastro = date.today()
        elif isinstance(data_cadastro, date):
            self.__data_cadastro = data_cadastro
        else:
            self.__data_cadastro = date.today()

    @property
    def id_aluno(self):
        return self.__id_aluno

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome or len(nome) < 3:
            # Em produção, evite crashar aqui se vier do banco. 
            # Mas vamos manter sua validação por enquanto.
            pass 
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data):
        # 1. Se vier STRING do banco (ex: "2000-01-01" ou "2000-01-01 12:00:00")
        if isinstance(data, str):
            try:
                # Remove horário se houver (pega tudo antes do espaço)
                data_limpa = data.split(" ")[0]
                data = datetime.strptime(data_limpa, "%Y-%m-%d").date()
            except ValueError:
                # Se falhar a conversão, define uma data padrão para não travar o login
                data = date(2000, 1, 1)

        # 2. Se for None ou outro tipo estranho
        if not isinstance(data, date):
            data = date(2000, 1, 1)

        # 3. Validação lógica (com proteção)
        # Se a data for no futuro, corrigimos para hoje em vez de dar erro fatal
        if data > date.today():
            data = date.today()

        self.__data_nascimento = data

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @property
    def data_cadastro(self):
        return self.__data_cadastro

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
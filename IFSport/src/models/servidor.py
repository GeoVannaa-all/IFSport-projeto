class Servidor:
    def __init__(self, id_servidor, nome, email, senha, cargo, data_cadastro):
        self.__id_servidor = id_servidor
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__cargo = cargo
        self.__data_cadastro = data_cadastro

    def get_id_servidor(self):
        return self.__id_servidor
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha
    def get_cargo(self):
        return self.__cargo
    def get_data_cadastro(self):
        return self.__data_cadastro

    def set_id_servidor(self, id_servidor):
        self.__id_servidor = id_servidor
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_senha(self, senha):
        self.__senha = senha
    def set_cargo(self, cargo):
        self.__cargo = cargo
    def set_data_cadastro(self, data_cadastro):
        self.__data_cadastro = data_cadastro

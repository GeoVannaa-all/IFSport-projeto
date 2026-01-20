from datetime import datetime

class Servidor:
    def __init__(self, id_servidor, nome, email, senha, cargo, data_cadastro):
        self.__id_servidor = id_servidor
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.__data_cadastro = data_cadastro

    @property
    def id_servidor(self):
        return self.__id_servidor

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
        if len(senha) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        self.__senha = senha

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        if not cargo:
            raise ValueError("Cargo obrigatório")
        self.__cargo = cargo

    @property
    def data_cadastro(self):
        return self.__data_cadastro

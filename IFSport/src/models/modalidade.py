class Modalidade:
    def __init__(self, id_modalidade, nome, descricao, vagas, status):
        self.__id_modalidade = id_modalidade
        self.__nome = nome
        self.__descricao = descricao
        self.__vagas = vagas
        self.__status = status


    def get_id_modalidade(self):
        return self.__id_modalidade
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    def get_vagas(self):
        return self.__vagas
    def get_status(self):
        return self.__status

    def set_id_modalidade(self, id_modalidade):
        self.__id_modalidade = id_modalidade
    def set_nome(self, nome):
        self.__nome = nome
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_vagas(self, vagas):
        self.__vagas = vagas
    def set_status(self, status):
        self.__status = status

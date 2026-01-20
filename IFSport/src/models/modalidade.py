class Modalidade:
    def __init__(self, id_modalidade, nome, descricao, vagas, status):
        self.__id_modalidade = id_modalidade
        self.nome = nome
        self.descricao = descricao
        self.vagas = vagas
        self.status = status

   
    @property
    def id_modalidade(self):
        return self.__id_modalidade

   
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome or len(nome) < 3:
            raise ValueError("Nome da modalidade inválido")
        self.__nome = nome

   
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not descricao:
            raise ValueError("Descrição obrigatória")
        self.__descricao = descricao

    
    @property
    def vagas(self):
        return self.__vagas

    @vagas.setter
    def vagas(self, vagas):
        if vagas <= 0:
            raise ValueError("Número de vagas inválido")
        self.__vagas = vagas

   
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status not in ("ATIVA", "INATIVA"):
            raise ValueError("Status inválido")
        self.__status = status


# from enum import Enum

# class StatusModalidade(Enum):
#     ATIVA = "ATIVA"
#     INATIVA = "INATIVA"

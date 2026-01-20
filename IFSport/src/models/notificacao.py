from datetime import datetime

class Notificacao:
    def __init__(self, id_notificacao, mensagem, data_envio, lida, id_aluno, id_servidor):

        self.__id_notificacao = id_notificacao
        self.mensagem = mensagem
        self.data_envio = data_envio
        self.lida = lida
        self.id_aluno = id_aluno
        self.id_servidor = id_servidor

    @property
    def id_notificacao(self):
        return self.__id_notificacao

   
    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        if not mensagem:
            raise ValueError("Mensagem não pode ser vazia")
        self.__mensagem = mensagem

     
    @property
    def data_envio(self):
        return self.__data_envio

    @data_envio.setter
    def data_envio(self, data_envio):
        if not isinstance(data_envio, datetime):
            raise ValueError("Data de envio inválida")
        self.__data_envio = data_envio

 
    @property
    def lida(self):
        return self.__lida

    @lida.setter
    def lida(self, lida):
        if not isinstance(lida, bool):
            raise ValueError("Lida deve ser booleano")
        self.__lida = lida

    def marcar_como_lida(self):
        self.__lida = True

    @property
    def id_aluno(self):
        return self.__id_aluno

    @id_aluno.setter
    def id_aluno(self, id_aluno):
        if id_aluno is None:
            raise ValueError("ID do aluno inválido")
        self.__id_aluno = id_aluno

    @property
    def id_servidor(self):
        return self.__id_servidor

    @id_servidor.setter
    def id_servidor(self, id_servidor):
        if id_servidor is None:
            raise ValueError("ID do servidor inválido")
        self.__id_servidor = id_servidor

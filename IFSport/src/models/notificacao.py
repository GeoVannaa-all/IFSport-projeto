class Notificacao:
    def __init__(self, id_notificacao, mensagem, data_envio, lida, id_aluno, id_servidor):
        self.__id_notificacao = id_notificacao
        self.__mensagem = mensagem
        self.__data_envio = data_envio
        self.__lida = lida
        self.__id_aluno = id_aluno
        self.__id_servidor = id_servidor


    def get_id_notificacao(self):
        return self.__id_notificacao
    def get_mensagem(self):
        return self.__mensagem
    def get_data_envio(self):
        return self.__data_envio
    def get_lida(self):
        return self.__lida
    def get_id_aluno(self):
        return self.__id_aluno
    def get_id_servidor(self):
        return self.__id_servidor

 
    def set_id_notificacao(self, id_notificacao):
        self.__id_notificacao = id_notificacao
    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem
    def set_data_envio(self, data_envio):
        self.__data_envio = data_envio
    def set_lida(self, lida):
        self.__lida = lida
    def set_id_aluno(self, id_aluno):
        self.__id_aluno = id_aluno
    def set_id_servidor(self, id_servidor):
        self.__id_servidor = id_servidor

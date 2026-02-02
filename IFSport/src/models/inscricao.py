class Inscricao:
    def __init__(self, id_inscricao=None, data_inscricao=None, status=None, id_aluno=None, id_modalidade=None):
        self._id_inscricao = id_inscricao
        self._data_inscricao = data_inscricao
        self._status = status
        self._id_aluno = id_aluno
        self._id_modalidade = id_modalidade

    @property
    def id_inscricao(self):
        return self._id_inscricao

    @property
    def data_inscricao(self):
        return self._data_inscricao

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        # Exemplo de validação no Setter
        status_validos = ["Ativo", "Pendente", "Cancelado"]
        if valor not in status_validos:
            # Apenas aviso, ou poderia lançar erro
            print(f"Aviso: Status '{valor}' incomum.") 
        self._status = valor

    @property
    def id_aluno(self):
        return self._id_aluno

    @property
    def id_modalidade(self):
        return self._id_modalidade
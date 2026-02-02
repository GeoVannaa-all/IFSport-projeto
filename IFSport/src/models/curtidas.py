class Curtida:
    def __init__(self, id_curtida=None, id_aluno=None, id_postagem=None):
        self._id_curtida = id_curtida
        self._id_aluno = id_aluno
        self._id_postagem = id_postagem

    @property
    def id_curtida(self): return self._id_curtida

    @property
    def id_aluno(self): return self._id_aluno
    
    @id_aluno.setter
    def id_aluno(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("ID do aluno inválido.")
        self._id_aluno = valor

    @property
    def id_postagem(self): return self._id_postagem
    
    @id_postagem.setter
    def id_postagem(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("ID da postagem inválido.")
        self._id_postagem = valor
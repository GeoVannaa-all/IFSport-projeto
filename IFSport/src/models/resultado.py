class Resultado:
    def __init__(self, id_seletiva=None, id_aluno=None, resultado=None, observacao=None):
        self._id_seletiva = id_seletiva
        self._id_aluno = id_aluno
        self._resultado = resultado
        self._observacao = observacao

    @property
    def id_seletiva(self): return self._id_seletiva

    @property
    def id_aluno(self): return self._id_aluno

    @property
    def resultado(self):
        return self._resultado

    @resultado.setter
    def resultado(self, valor):
        opcoes_validas = ["Aprovado", "Reprovado", "Lista de Espera"]
        if valor not in opcoes_validas:
             # Aqui usamos ValueError para forçar que seja uma das opções
            raise ValueError(f"Resultado inválido. Opções: {opcoes_validas}")
        self._resultado = valor

    @property
    def observacao(self):
        return self._observacao

    @observacao.setter
    def observacao(self, valor):
        self._observacao = valor
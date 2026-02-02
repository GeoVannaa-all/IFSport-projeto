class Seletiva:
    def __init__(self, id_seletiva=None, data=None, local=None, criterio=None, id_modalidade=None):
        self._id_seletiva = id_seletiva
        self._data = data
        self._local = local
        self._criterio = criterio
        self._id_modalidade = id_modalidade

    @property
    def id_seletiva(self):
        return self._id_seletiva

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        if not valor:
            raise ValueError("A data da seletiva é obrigatória.")
        self._data = valor

    @property
    def local(self):
        return self._local
    
    @local.setter
    def local(self, valor):
        if not valor or len(valor) < 3:
            raise ValueError("O local da seletiva deve ser informado corretamente.")
        self._local = valor

    @property
    def criterio(self):
        return self._criterio
    
    @criterio.setter
    def criterio(self, valor):
        # Criterio é opcional, mas se vier, não pode ser gigantesco
        if valor and len(valor) > 200:
            raise ValueError("O critério é muito longo.")
        self._criterio = valor

    @property
    def id_modalidade(self):
        return self._id_modalidade
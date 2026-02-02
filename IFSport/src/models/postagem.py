class Postagem:
    def __init__(self, id_postagem=None, titulo=None, conteudo=None, imagem=None, data_postagem=None, id_servidor=None):
     
        self._id_postagem = id_postagem
        self._titulo = titulo
        self._conteudo = conteudo
        self._imagem = imagem
        self._data_postagem = data_postagem
        self._id_servidor = id_servidor

  

    @property
    def id_postagem(self):
        return self._id_postagem

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("O título não pode ser vazio.")
        self._titulo = valor

    @property
    def conteudo(self):
        return self._conteudo

    @conteudo.setter
    def conteudo(self, valor):
        self._conteudo = valor

    @property
    def imagem(self):
        return self._imagem
    
    @property
    def data_postagem(self):
        return self._data_postagem

    @property
    def id_servidor(self):
        return self._id_servidor

    def __repr__(self):
        return f"Postagem(id={self._id_postagem}, titulo={self._titulo})"
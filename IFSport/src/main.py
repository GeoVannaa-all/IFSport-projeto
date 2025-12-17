from database import Database
from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository


db = Database()
db.criar_tabelas()


aluno = Aluno(
    nome="João Luis",
    email="joao@email.com",
    senha="202410",
    curso="Informática"
)

#Salvar no banco
repo = AlunoRepository()
repo.salvar(aluno)

#Ler do banco
alunos = repo.listar()
for a in alunos:
    print(a.id_aluno, a.nome, a.email, a.curso)

import streamlit as st
import sys
import os


diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(diretorio_atual)


from database.database import Database
from dao.aluno_repository import AlunoRepository
# Alterado para usar o AdminRepository que criamos no passo anterior
from dao.admin_repository import AdminRepository 
from templates.styles import carregar_estilos 

from views.pages.login_UI import login_page
from views.pages.aluno_home_UI import aluno_dashboard
# Certifique-se que este arquivo existe (vamos criar/ajustar ele a seguir se precisar)
from views.pages.admin_home_UI import servidor_dashboard 


st.set_page_config(page_title="IFSPORT", layout="wide")

try:
    carregar_estilos()
except Exception as e:
    # Apenas um print no console para não sujar a tela se falhar o CSS
    print(f"Estilos não carregados: {e}")


if "db" not in st.session_state:
    st.session_state.db = Database()

# Instanciando os repositórios corretos
aluno_repo = AlunoRepository(st.session_state.db)
admin_repo = AdminRepository(st.session_state.db) 

# Inicialização de Variáveis de Estado (Sem duplicatas)
if "page" not in st.session_state:
    st.session_state.page = "login"

if "aluno_logado" not in st.session_state:
    st.session_state.aluno_logado = None

# MUDANÇA IMPORTANTE: Usando 'admin_logado' para combinar com o login_UI
if "admin_logado" not in st.session_state:
    st.session_state.admin_logado = None

if "aluno_action" not in st.session_state:
    st.session_state.aluno_action = "login"



if st.session_state.page == "login":
    # Passamos o admin_repo atualizado aqui
    login_page(aluno_repo, admin_repo)

elif st.session_state.page == "dashboard_aluno":
    if st.session_state.aluno_logado:
        aluno_dashboard(st.session_state.db)
    else:
        st.warning("Acesso restrito. Faça login.")
        st.session_state.page = "login"
        st.rerun()

elif st.session_state.page == "dashboard_admin":
    # Verificação correta usando admin_logado
    if st.session_state.admin_logado:
        servidor_dashboard(st.session_state.db)
    else:
        st.warning("Acesso restrito a administradores.")
        st.session_state.page = "login"
        st.rerun()
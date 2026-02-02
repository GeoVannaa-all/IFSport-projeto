import streamlit as st
from repositories.database import Database
from repositories.aluno_repository import AlunoRepository
from repositories.servidor_repository import ServidorRepository

from templates.styles import carregar_estilos
from views.auth_view import login_page
from views.aluno_view import aluno_dashboard
from views.servidor_view import servidor_dashboard

st.set_page_config(page_title="IFSPORT", layout="wide")
carregar_estilos()

# =========================
# DATABASE
# =========================
db = Database()

# =========================
# REPOSITÓRIOS BASE
# =========================
aluno_repo = AlunoRepository(db)
servidor_repo = ServidorRepository()

# =========================
# SESSION STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "login"

if "aluno_logado" not in st.session_state:
    st.session_state.aluno_logado = None

if "aluno_action" not in st.session_state:
    st.session_state.aluno_action = None

if "menu" not in st.session_state:
    st.session_state.menu = "feed"

if "menu_admin" not in st.session_state:
    st.session_state.menu_admin = "postagens"

# =========================
# ROTAS
# =========================
if st.session_state.page == "login":
    login_page(aluno_repo, servidor_repo)

elif st.session_state.page == "dashboard_aluno":
    aluno_dashboard(db)

elif st.session_state.page == "dashboard_admin":
    servidor_dashboard(db)

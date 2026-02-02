import streamlit as st
import sys
import os

# ==================================================
# 1. CORREÇÃO DE CAMINHO (O "Pulo do Gato")
# ==================================================
# Isso garante que o Python encontre as pastas dao, views, etc.
# independentemente de onde você roda o comando.
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(diretorio_atual)

# ==================================================
# 2. IMPORTS CORRIGIDOS (Baseados nas suas imagens)
# ==================================================
from database.database import Database
from dao.aluno_repository import AlunoRepository
from dao.servidor_repository import ServidorRepository
from templates.styles import carregar_estilos 

# Imports das VIEWS (Caminho correto: views.pages.nome_do_arquivo)
from views.pages.login_UI import login_page
from views.pages.aluno_home_UI import aluno_dashboard

# ATENÇÃO: Na sua imagem o arquivo é 'admin_home_UI.py', corrigi aqui:
from views.pages.admin_home_UI import servidor_dashboard 

# ==================================================
# 3. CONFIGURAÇÃO DA PÁGINA
# ==================================================
st.set_page_config(page_title="IFSPORT", layout="wide")

# Tenta carregar estilos, se der erro avisa (pra não travar o app)
try:
    carregar_estilos()
except Exception as e:
    print(f"Aviso: Não foi possível carregar estilos: {e}")

# ==================================================
# 4. INICIALIZAÇÃO DO BANCO E REPOSITÓRIOS
# ==================================================
if "db" not in st.session_state:
    st.session_state.db = Database()

# Correção Lógica: Passando o 'db' para ambos os repositórios
aluno_repo = AlunoRepository(st.session_state.db)
servidor_repo = ServidorRepository(st.session_state.db) 


if "page" not in st.session_state:
    st.session_state.page = "login"

if "aluno_logado" not in st.session_state:
    st.session_state.aluno_logado = None

if "servidor_logado" not in st.session_state:
    st.session_state.servidor_logado = None

if "menu" not in st.session_state:
    st.session_state.menu = "feed"

if "menu_admin" not in st.session_state:
    st.session_state.menu_admin = "postagens"

if "page" not in st.session_state:
    st.session_state.page = "login"

if "aluno_logado" not in st.session_state:
    st.session_state.aluno_logado = None

if "servidor_logado" not in st.session_state:
    st.session_state.servidor_logado = None


if "aluno_action" not in st.session_state:
    st.session_state.aluno_action = "login"  # Define o padrão como 'login'


if "menu" not in st.session_state:
    st.session_state.menu = "feed"

if "menu_admin" not in st.session_state:
    st.session_state.menu_admin = "postagens"


if st.session_state.page == "login":
    login_page(aluno_repo, servidor_repo)

elif st.session_state.page == "dashboard_aluno":
    if st.session_state.aluno_logado:
        aluno_dashboard(st.session_state.db)
    else:
        st.session_state.page = "login"
        st.rerun()

elif st.session_state.page == "dashboard_admin":
    # Supondo que você vá implementar login de admin depois
    servidor_dashboard(st.session_state.db)
import streamlit as st
from repositories.aluno_repository import AlunoRepository
from repositories.servidor_repository import ServidorRepository
from repositories.modalidade_repository import ModalidadeRepository
from repositories.database import Database
from datetime import date

# ================= CONFIG =================
st.set_page_config(page_title="IFSPORT", layout="wide")

# ================= BANCO =================
db = Database()
aluno_repo = AlunoRepository(db)
servidor_repo = ServidorRepository()
modalidade_repo = ModalidadeRepository(db)

# ================= SESSÃO =================
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

# ================= ESTILO =================
st.markdown("""
<style>
body {
    background-color: #f4f6f8;
}

.header-title {
    font-size: 26px;
    font-weight: bold;
    color: #006400;
}

.main-container {
    max-width: 1000px;
    margin: auto;
    padding-top: 20px;
}

.card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 18px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
def login_page():
    st.title("IFSPORT")
    st.subheader("Sistema Esportivo Institucional")

    user_type = st.sidebar.selectbox(
        "Quem está entrando?",
        ["Aluno", "Admin"],
        key="tipo_usuario"
    )

    if user_type == "Aluno":
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Entrar", key="btn_entrar_aluno"):
                st.session_state.aluno_action = "login"

        with col2:
            if st.button("Cadastrar", key="btn_cadastrar_aluno"):
                st.session_state.aluno_action = "cadastro"

        if st.session_state.aluno_action == "login":
            mostrar_login_aluno()
        elif st.session_state.aluno_action == "cadastro":
            mostrar_cadastro_aluno()

    else:
        st.subheader("Login do Administrador")
        senha_admin = st.text_input("Senha", type="password", key="senha_admin")

        if st.button("Entrar como Admin", key="btn_login_admin"):
            if senha_admin == "1234":
                st.session_state.page = "dashboard_admin"
            else:
                st.error("Senha incorreta")

def mostrar_login_aluno():
    st.subheader("Login do Aluno")

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", key="btn_login_aluno"):
        aluno = aluno_repo.login_aluno(email, senha)
        if aluno:
            st.session_state.aluno_logado = (aluno[0], aluno[1])
            st.session_state.page = "dashboard_aluno"
        else:
            st.error("Email ou senha inválidos")

def mostrar_cadastro_aluno():
    st.subheader("Cadastro do Aluno")

    nome = st.text_input("Nome", key="cad_nome")
    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    data_nascimento = st.date_input(
        "Data de Nascimento",
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        key="cad_data"
    )
    matricula = st.text_input("Matrícula", key="cad_matricula")

    curso = st.selectbox(
        "Curso",
        [
            "Infoweb",
            "Administração",
            "MSI",
            "Controle Ambiental",
            "Mineração",
            "Geologia",
            "Edificações",
            "Eletrotécnica",
            "Mecânica"
        ],
        key="cad_curso"
    )

    if st.button("Cadastrar", key="btn_confirmar_cadastro"):
        aluno_repo.cadastrar_aluno(
            nome,
            email,
            senha,
            data_nascimento.isoformat(),
            matricula,
            curso
        )
        st.success("Cadastro realizado com sucesso!")
        st.session_state.aluno_action = "login"

# ================= LOGOUT =================
def logout():
    st.session_state.page = "login"
    st.session_state.aluno_logado = None
    st.session_state.aluno_action = None

# ================= DASHBOARD ALUNO =================
def aluno_dashboard():
    aluno_id, aluno_nome = st.session_state.aluno_logado

    # ===== HEADER =====
    col1, col2 = st.columns([3, 7])

    with col1:
        st.markdown("<div class='header-title'>IFSPORT</div>", unsafe_allow_html=True)

    with col2:
        b1, b2, b3 = st.columns(3)

        if b1.button("📰 Feed", key="menu_feed"):
            st.session_state.menu = "feed"

        if b2.button("👤 Perfil", key="menu_perfil"):
            st.session_state.menu = "perfil"

        if b3.button("🚪 Sair", key="menu_logout"):
            logout()

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    # ===== CONTEÚDO =====
    if st.session_state.menu == "feed":
        st.subheader("📰 Feed de Notícias")

        for i in range(3):
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### Processo Seletivo Esportivo")
            st.write("Inscrições abertas para modalidades esportivas.")
            st.button("❤️ Curtir", key=f"like_{i}")
            st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.menu == "perfil":
        st.subheader("👤 Meu Perfil")
        st.write(f"**Nome:** {aluno_nome}")
        st.write(f"**ID:** {aluno_id}")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= DASHBOARD ADMIN =================
def servidor_dashboard():
    col1, col2 = st.columns([3, 7])

    with col1:
        st.markdown("<div class='header-title'>Admin IFSPORT</div>", unsafe_allow_html=True)

    with col2:
        b1, b2, b3, b4 = st.columns(4)

        if b1.button("📝 Postagens", key="admin_postagens"):
            st.session_state.menu_admin = "postagens"

        if b2.button("✅ Aprovações", key="admin_aprovacoes"):
            st.session_state.menu_admin = "aprovacoes"

        if b3.button("🏅 Modalidades", key="admin_modalidades"):
            st.session_state.menu_admin = "modalidades"

        if b4.button("🚪 Sair", key="admin_logout"):
            logout()

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    if st.session_state.menu_admin == "postagens":
        st.subheader("📝 Criar Postagem")
        st.text_input("Título", key="post_titulo")
        st.text_area("Conteúdo", key="post_conteudo")
        st.button("Publicar", key="btn_publicar")

    elif st.session_state.menu_admin == "aprovacoes":
        st.subheader("✅ Inscrições Pendentes")
        st.write("Aluno X — Modalidade Y")
        st.button("Aprovar", key="btn_aprovar")

    elif st.session_state.menu_admin == "modalidades":
        st.subheader("🏅 Criar Modalidade")
        st.text_input("Nome da modalidade", key="mod_nome")
        st.number_input("Vagas", min_value=1, key="mod_vagas")
        st.button("Salvar", key="btn_salvar_modalidade")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CONTROLE =================
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "dashboard_aluno":
    aluno_dashboard()
elif st.session_state.page == "dashboard_admin":
    servidor_dashboard()

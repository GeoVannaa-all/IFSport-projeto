import streamlit as st
from repositories.aluno_repository import AlunoRepository
from repositories.servidor_repository import ServidorRepository
from repositories.database import Database
from datetime import date


st.set_page_config(page_title="IFSPORT", layout="wide")


# Banco e Repositórios

db = Database()
aluno_repo = AlunoRepository(db)
servidor_repo = ServidorRepository()  # Admin com senha fixa


# Variáveis de sessão

if "page" not in st.session_state:
    st.session_state.page = "login"  # login, dashboard_aluno, dashboard_admin
if "aluno_logado" not in st.session_state:
    st.session_state.aluno_logado = None  # Guarda tupla (id_aluno, nome)
if "aluno_action" not in st.session_state:
    st.session_state.aluno_action = None  # login ou cadastro


st.markdown("""
<style>
.button-style {
    background-color: #006400;
    color: white;
    padding: 10px 25px;
    margin: 5px;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
}
.button-style:hover {
    background-color: #228B22;
}

.profile-container {
    background-color: #6dab5d;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
}

.profile-container img {
    width: 300px;  
    height: 300px;
    border-radius: 50%; 
    object-fit: cover;  
}

.header {
    background-color: #006400;
    color: white;
    padding: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


def login_page():
    st.title("IFSPORT - Login")
    user_type = st.sidebar.selectbox("Quem está entrando?", ["Aluno", "Admin"])

    if user_type == "Aluno":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Entrar"):
                st.session_state.aluno_action = "login"
        with col2:
            if st.button("Cadastrar"):
                st.session_state.aluno_action = "cadastro"

        if st.session_state.aluno_action == "login":
            mostrar_login_aluno()
        elif st.session_state.aluno_action == "cadastro":
            mostrar_cadastro_aluno()

    elif user_type == "Admin":
        st.subheader("Login do Admin")
        senha_admin = st.text_input("Senha", type="password")
        if st.button("Login Admin"):
            if senha_admin == "1234":
                st.session_state.page = "dashboard_admin"
            else:
                st.error("Senha incorreta")


def mostrar_login_aluno():
    st.write("### Login do Aluno")
    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")
    if st.button("Entrar Aluno"):
        aluno = aluno_repo.login_aluno(email, senha)
        if aluno:
            st.session_state.aluno_logado = (aluno[0], aluno[1])  # id, nome
            st.session_state.page = "dashboard_aluno"
        else:
            st.error("Email ou senha incorretos")

def mostrar_cadastro_aluno():
    st.write("### Cadastro do Aluno")
    nome = st.text_input("Nome", key="cad_nome")
    email = st.text_input("Email", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    data_nascimento = st.date_input(
        "Data de Nascimento",
        min_value=date(1900,1,1),
        max_value=date.today(),
        key="cad_data"
    )
    matricula = st.text_input("Matrícula", key="cad_matricula")
    curso = st.text_input("Curso", key="cad_curso")

    if st.button("Cadastrar Aluno"):
        if nome and email and senha and data_nascimento and matricula and curso:
            try:
                aluno_repo.cadastrar_aluno(
                    nome, email, senha, data_nascimento.isoformat(), matricula, curso
                )
                st.success("Cadastro realizado! Agora faça login")
                st.session_state.aluno_action = "login"
            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")
        else:
            st.warning("Preencha todos os campos")

def aluno_dashboard():
    aluno_id, aluno_nome = st.session_state.aluno_logado
    st.subheader(f"Olá, {aluno_nome}!")

    # Divide a tela em 2 colunas
    col1, col2 = st.columns([3, 1])

    with col1:
        menu = st.radio(
            "Escolha uma opção:",
            ["Feed", "Inscrever-se em Modalidade", "Histórico de Inscrições", "Notificações"],
            horizontal=True
        )

        if menu == "Feed":
            st.write("### Feed de Notícias")
            st.write("Aqui você verá as últimas notícias e postagens esportivas.")
        elif menu == "Inscrever-se em Modalidade":
            st.write("### Inscrição em Modalidades")
            st.write("Aqui você pode se inscrever nas modalidades disponíveis.")
        elif menu == "Histórico de Inscrições":
            st.write("### Histórico de Inscrições")
            st.write("Aqui você verá todas as suas inscrições.")
        elif menu == "Notificações":
            st.write("### Notificações")
            st.write("Aqui estão suas notificações.")

        # Logout
        if st.button("Sair"):
            st.session_state.aluno_logado = None
            st.session_state.page = "login"

    with col2:
        # Perfil do aluno à direita
        # st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        # Foto de perfil que está na pasta assets
        st.image("assets/perfil.jpg", caption="Foto de Perfil", width=300)
        st.write(f"**Nome**: {aluno_nome}")
        st.write(f"**Matrícula**: {aluno_id}")
        st.write(f"**Curso**: Exemplo de Curso")

        # Histórico de inscrições
        st.subheader("Histórico de Inscrições")
        st.write("Aqui aparecerão todas as suas inscrições passadas.")
        st.write("- Modalidade A (Aprovado)")
        st.write("- Modalidade B (Pendente)")

        # Inscrições aprovadas
        st.subheader("Inscrições Aprovadas")
        st.write("Você foi aprovado nas seguintes modalidades:")
        st.write("- Modalidade A")


def servidor_dashboard():
    menu = st.radio(
        "Menu do Admin:",
        ["Gerenciar Postagens", "Gerenciar Notificações", "Gerenciar Modalidades"],
        horizontal=True
    )

    if menu == "Gerenciar Postagens":
        st.write("### Gerenciar Postagens")
        st.write("Aqui você pode criar, editar ou deletar postagens.")
    elif menu == "Gerenciar Notificações":
        st.write("### Gerenciar Notificações")
        st.write("Aqui você pode criar ou enviar notificações para alunos.")
    elif menu == "Gerenciar Modalidades":
        st.write("### Gerenciar Modalidades")
        st.write("Aqui você pode criar ou editar modalidades.")

    if st.button("Sair do Admin"):
        st.session_state.page = "login"

if __name__ == "__main__":
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "dashboard_aluno":
        aluno_dashboard()
    elif st.session_state.page == "dashboard_admin":
        servidor_dashboard()

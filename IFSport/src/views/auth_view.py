import streamlit as st
from datetime import date

def login_page(aluno_repo, servidor_repo):
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
            if st.button("Entrar", key="btn_ir_login"):
                st.session_state.aluno_action = "login"

        with col2:
            if st.button("Cadastrar", key="btn_ir_cadastro"):
                st.session_state.aluno_action = "cadastro"

        if st.session_state.aluno_action == "login":
            mostrar_login_aluno(aluno_repo)
        elif st.session_state.aluno_action == "cadastro":
            mostrar_cadastro_aluno(aluno_repo)

    else:
        mostrar_login_admin(servidor_repo)


def mostrar_login_aluno(aluno_repo):
    st.subheader("Login do Aluno")

    email = st.text_input("Email", key="login_email")
    senha = st.text_input("Senha", type="password", key="login_senha")

    if st.button("Entrar", key="btn_login_aluno"):
        aluno = aluno_repo.login_aluno(email, senha)
        if aluno:
            st.session_state.aluno_logado = (aluno.id_aluno, aluno.nome)
            st.session_state.page = "dashboard_aluno"
        else:
            st.error("Email ou senha inválidos")


def mostrar_cadastro_aluno(aluno_repo):
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
            "Infoweb","Administração","MSI","Controle Ambiental",
            "Mineração","Geologia","Edificações","Eletrotécnica","Mecânica"
        ],
        key="cad_curso"
    )

    if st.button("Cadastrar", key="btn_confirmar_cadastro"):
        aluno_repo.cadastrar(
            nome, email, senha,
            data_nascimento.isoformat(),
            matricula, curso
        )
        st.success("Cadastro realizado com sucesso!")
        st.session_state.aluno_action = "login"


def mostrar_login_admin(servidor_repo):
    st.subheader("Login do Administrador")

    senha_admin = st.text_input(
        "Senha",
        type="password",
        key="senha_admin"
    )

    if st.button("Entrar como Admin", key="btn_login_admin"):
        if servidor_repo.login_admin(senha_admin):
            st.session_state.page = "dashboard_admin"
        else:
            st.error("Senha incorreta")

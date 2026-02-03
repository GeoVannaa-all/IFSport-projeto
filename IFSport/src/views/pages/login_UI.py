import streamlit as st
from datetime import date
import time

def login_page(aluno_repo, servidor_repo):
    st.title("IFSPORT")
    st.subheader("Sistema Esportivo Institucional")

    # Sidebar para escolher o tipo de usuário
    user_type = st.sidebar.selectbox(
        "Quem está entrando?",
        ["Aluno", "Admin"],
        key="tipo_usuario"
    )

    if user_type == "Aluno":
        # Lógica de alternância entre Login e Cadastro do Aluno
        if "aluno_action" not in st.session_state:
            st.session_state.aluno_action = "login"

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Entrar", key="btn_ir_login", use_container_width=True):
                st.session_state.aluno_action = "login"
        with col2:
            if st.button("Cadastrar", key="btn_ir_cadastro", use_container_width=True):
                st.session_state.aluno_action = "cadastro"

        st.markdown("---") # Linha separadora visual

        if st.session_state.aluno_action == "login":
            mostrar_login_aluno(aluno_repo)
        elif st.session_state.aluno_action == "cadastro":
            mostrar_cadastro_aluno(aluno_repo)

    else:
        # Se for Admin, mostra o login de Admin
        mostrar_login_admin(servidor_repo)


def mostrar_login_aluno(aluno_repo):
    st.subheader("🎓 Login do Aluno")

    email = st.text_input("Email", key="login_email_aluno")
    senha = st.text_input("Senha", type="password", key="login_senha_aluno")

    if st.button("Entrar", key="btn_login_aluno", type="primary"):
        aluno = aluno_repo.login_aluno(email, senha)
        
        if aluno:
            # O repo retorna um objeto ou tupla com os dados
            # Ajuste os índices conforme seu retorno (id, nome)
            st.session_state.aluno_logado = (aluno.id_aluno, aluno.nome)
            st.session_state.admin_logado = None # Limpa sessão de admin
            st.success(f"Bem-vindo(a), {aluno.nome}!")
            time.sleep(1)
            st.session_state.page = "dashboard_aluno"
            st.rerun()
        else:
            st.error("Email ou senha inválidos.")


def mostrar_cadastro_aluno(aluno_repo):
    st.subheader("📝 Cadastro de Novo Aluno")

    nome = st.text_input("Nome Completo", key="cad_nome")
    email = st.text_input("Email Institucional", key="cad_email")
    senha = st.text_input("Senha", type="password", key="cad_senha")
    
    c1, c2 = st.columns(2)
    with c1:
        data_nascimento = st.date_input(
            "Data de Nascimento",
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            key="cad_data"
        )
    with c2:
        matricula = st.text_input("Matrícula", key="cad_matricula")

    curso = st.selectbox(
        "Curso",
        [
            "Infoweb","Administração","MSI","Controle Ambiental",
            "Mineração","Geologia","Edificações","Eletrotécnica","Mecânica"
        ],
        key="cad_curso"
    )

    if st.button("Confirmar Cadastro", key="btn_confirmar_cadastro", type="primary"):
        if nome and email and senha and matricula:
            try:
                aluno_repo.cadastrar(
                    nome, email, senha,
                    data_nascimento.isoformat(),
                    matricula, curso
                )
                st.success("Cadastro realizado com sucesso! Faça login agora.")
                time.sleep(2)
                st.session_state.aluno_action = "login"
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")
        else:
            st.warning("Preencha todos os campos obrigatórios.")


def mostrar_login_admin(servidor_repo):
    st.subheader("🛡️ Login Administrativo")
    st.caption("Área restrita para servidores e coordenação.")

    # Agora pedimos E-mail e Senha
    email_admin = st.text_input(
        "Email Institucional", 
        key="email_admin",
    )
    
    senha_admin = st.text_input(
        "Senha",
        type="password",
        key="senha_admin"
    )

    if st.button("Acessar Painel", key="btn_login_admin", type="primary"):
        # Chama o método que verifica email E senha no banco
        dados_admin = servidor_repo.login_admin(email_admin, senha_admin)
        
        if dados_admin:
            # dados_admin é a tupla (id_servidor, nome, cargo)
            id_servidor = dados_admin[0]
            nome_generico = dados_admin[1] # Ex: "Coordenação"
            cargo = dados_admin[2]

            st.session_state.admin_logado = (id_servidor, nome_generico)
            st.session_state.aluno_logado = None # Garante que não é aluno
            
            st.success(f"Login autorizado: {nome_generico} ({cargo})")
            time.sleep(1)
            st.session_state.page = "dashboard_admin"
            st.rerun()
        else:
            st.error("Credenciais inválidas ou acesso não autorizado.")
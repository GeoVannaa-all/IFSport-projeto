import streamlit as st
from repositories.aluno_repository import AlunoRepository
from repositories.servidor_repository import ServidorRepository
from repositories.database import Database

def login():
    st.title("IFSPORT - Login")

    user_type = st.selectbox("Quem está entrando?", ["Aluno", "Servidor"])

    if user_type == "Aluno":
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Login"):
            aluno_repo = AlunoRepository(Database())
            aluno = aluno_repo.validar_login(email, senha)
            if aluno:
                st.success(f"Bem-vindo, {aluno.nome}!")
                aluno_dashboard(aluno.id_aluno)
            else:
                st.error("Credenciais inválidas")

    elif user_type == "Servidor":
        email = st.text_input("Email do servidor")
        senha = st.text_input("Senha", type="password")

        if st.button("Login"):
            servidor_repo = ServidorRepository(Database())
            servidor = servidor_repo.validar_login(email, senha)
            if servidor:
                st.success(f"Bem-vindo, {servidor.nome}!")
                servidor_dashboard(servidor.id_servidor)
            else:
                st.error("Credenciais inválidas")

def aluno_dashboard(aluno_id):
    st.subheader("Menu do Aluno")
    option = st.selectbox("O que você deseja fazer?", ["Ver feed", "Inscrever-se", "Histórico de Inscrições", "Ver Notificações"])
    # Aqui você pode adicionar as funcionalidades

def servidor_dashboard(servidor_id):
    st.subheader("Menu do Servidor")
    option = st.selectbox("O que você deseja fazer?", ["Gerenciar Postagens", "Gerenciar Notificações"])
    # Aqui você pode adicionar as funcionalidades

if __name__ == "__main__":
    login()

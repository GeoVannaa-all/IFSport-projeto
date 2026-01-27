import streamlit as st

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

def logout():
    st.session_state.page = "login"

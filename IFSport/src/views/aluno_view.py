import streamlit as st

def aluno_dashboard():
    aluno_id, aluno_nome = st.session_state.aluno_logado

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

def logout():
    st.session_state.page = "login"
    st.session_state.aluno_logado = None
    st.session_state.aluno_action = None

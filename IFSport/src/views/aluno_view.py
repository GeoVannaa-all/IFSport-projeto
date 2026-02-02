import streamlit as st
from repositories.postagem_repository import PostagemRepository
from repositories.like_repository import LikeRepository
from repositories.modalidade_repository import ModalidadeRepository
from repositories.inscricao_repository import InscricaoRepository


def aluno_dashboard(db):
    # ======== ESTADO INICIAL ========
    if "menu" not in st.session_state:
        st.session_state.menu = "feed"

    aluno_id, aluno_nome = st.session_state.aluno_logado

    postagem_repo = PostagemRepository(db)
    like_repo = LikeRepository(db)
    modalidade_repo = ModalidadeRepository(db)
    inscricao_repo = InscricaoRepository(db)

    # ======== MENU SUPERIOR ========
    col1, col2 = st.columns([3, 7])

    with col1:
        st.markdown("<div class='header-title'>IFSPORT</div>", unsafe_allow_html=True)

    with col2:
        b1, b2, b3, b4 = st.columns(4)

        if b1.button("📰 Feed", key="menu_feed"):
            st.session_state.menu = "feed"

        if b2.button("📋 Inscrições", key="menu_insc"):
            st.session_state.menu = "inscricoes"

        if b3.button("👤 Perfil", key="menu_perfil"):
            st.session_state.menu = "perfil"

        if b4.button("🚪 Sair", key="menu_sair"):
            logout()

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    # ================= FEED =================
    if st.session_state.menu == "feed":
        st.subheader("📰 Feed de Notícias")

        postagens = postagem_repo.listar()

        for post in postagens:
            id_post, titulo, conteudo, _, _, _ = post

            curtidas = like_repo.contar(id_post)
            curtiu = like_repo.usuario_curtiu(id_post, aluno_id)

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"### {titulo}")
            st.write(conteudo)
            st.caption(f"❤️ {curtidas} curtida(s)")

            col1, _ = st.columns([2, 8])

            with col1:
                if not curtiu:
                    if st.button("❤️ Curtir", key=f"like_{id_post}"):
                        like_repo.curtir(aluno_id, id_post)  # ✅ ORDEM CORRETA
                        st.rerun()
                else:
                    if st.button("💔 Remover", key=f"unlike_{id_post}"):
                        like_repo.remover(aluno_id, id_post)  # ✅ ORDEM CORRETA
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    # ================= INSCRIÇÕES =================
    elif st.session_state.menu == "inscricoes":
        st.subheader("🏅 Modalidades Disponíveis")

        modalidades = modalidade_repo.listar_disponiveis()
        inscricoes_aluno = inscricao_repo.buscar_por_aluno(aluno_id)
        inscritas = {nome for nome, _ in inscricoes_aluno}

        for id_mod, nome, vagas in modalidades:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"### {nome}")
            st.write(f"🎯 Vagas disponíveis: {vagas}")

            if nome in inscritas:
                st.info("📌 Você já solicitou essa modalidade")
            elif vagas > 0:
                if st.button("📩 Solicitar vaga", key=f"sol_{id_mod}"):
                    inscricao_repo.solicitar(aluno_id, id_mod)
                    st.success("Solicitação enviada!")
                    st.rerun()
            else:
                st.error("❌ Sem vagas disponíveis")

            st.markdown("</div>", unsafe_allow_html=True)

        st.subheader("📌 Minhas Inscrições")

        for nome_mod, status in inscricoes_aluno:
            icone = {
                "PENDENTE": "🟡",
                "APROVADO": "🟢",
                "RECUSADO": "🔴"
            }.get(status, "⚪")

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.write(f"{icone} **{nome_mod}** — {status}")
            st.markdown("</div>", unsafe_allow_html=True)

    # ================= PERFIL =================
    elif st.session_state.menu == "perfil":
        st.subheader("👤 Meu Perfil")
        st.write(f"**Nome:** {aluno_nome}")
        st.write(f"**ID:** {aluno_id}")

    st.markdown("</div>", unsafe_allow_html=True)


def logout():
    st.session_state.page = "login"
    st.session_state.aluno_logado = None
    st.session_state.menu = "feed"

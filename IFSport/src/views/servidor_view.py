import streamlit as st

from repositories.postagem_repository import PostagemRepository
from repositories.modalidade_repository import ModalidadeRepository
from repositories.inscricao_repository import InscricaoRepository
from repositories.notificacao_repository import NotificacaoRepository


def servidor_dashboard(db):
    postagem_repo = PostagemRepository(db)
    modalidade_repo = ModalidadeRepository(db)
    inscricao_repo = InscricaoRepository(db)
    notificacao_repo = NotificacaoRepository(db)

    if "menu_admin" not in st.session_state:
        st.session_state.menu_admin = "postagens"

    # ===== HEADER =====
    col1, col2 = st.columns([3, 7])

    with col1:
        st.markdown("## 🛠️ Admin IFSPORT")

    with col2:
        b1, b2, b3, b4 = st.columns(4)

        if b1.button("📝 Postagens"):
            st.session_state.menu_admin = "postagens"

        if b2.button("🏅 Modalidades"):
            st.session_state.menu_admin = "modalidades"

        if b3.button("✅ Aprovações"):
            st.session_state.menu_admin = "aprovacoes"

        if b4.button("🚪 Sair"):
            logout()

    st.divider()

    # ================= POSTAGENS =================
    if st.session_state.menu_admin == "postagens":
        st.subheader("📝 Criar Postagem")

        titulo = st.text_input("Título")
        conteudo = st.text_area("Conteúdo")

        if st.button("Publicar"):
            postagem_repo.criar(titulo, conteudo, None, 1)
            st.success("Postagem criada!")
            st.rerun()

        st.divider()
        st.subheader("📰 Feed")

        postagens = postagem_repo.listar()

        for id_post, titulo, conteudo, *_ in postagens:
            st.markdown("----")
            st.markdown(f"### {titulo}")
            st.write(conteudo)

            if st.button("🗑️ Apagar", key=f"del_post_{id_post}"):
                postagem_repo.excluir(id_post)
                st.rerun()

    # ================= MODALIDADES =================
    elif st.session_state.menu_admin == "modalidades":
        st.subheader("🏅 Criar Modalidade")

        nome = st.text_input("Nome da modalidade")
        vagas_max = st.number_input("Vagas máximas", min_value=1, step=1)

        if st.button("Salvar Modalidade"):
            modalidade_repo.criar(nome, vagas_max)
            st.success("Modalidade criada!")
            st.rerun()

        st.divider()
        st.subheader("📋 Modalidades Criadas")

        modalidades = modalidade_repo.listar_todas()

        for id_mod, nome, vagas_max in modalidades:
            aprovados = inscricao_repo.contar_aprovados(id_mod)
            lista_aprovados = inscricao_repo.listar_aprovados_por_modalidade(id_mod)

            st.markdown("----")
            st.markdown(f"### 🏅 {nome}")
            st.write(f"👥 Participantes: **{aprovados}/{vagas_max}**")

            if aprovados >= vagas_max:
                st.error("🔒 Modalidade ENCERRADA")

            for aluno, matricula in lista_aprovados:
                st.write(f"• {aluno} — {matricula}")

            if st.button("🗑️ Excluir Modalidade", key=f"del_mod_{id_mod}"):
                modalidade_repo.excluir(id_mod)
                st.success("Modalidade excluída!")
                st.rerun()

    # ================= APROVAÇÕES =================
    elif st.session_state.menu_admin == "aprovacoes":
        st.subheader("✅ Inscrições Pendentes")

        pendentes = inscricao_repo.listar_pendentes()

        if not pendentes:
            st.info("Nenhuma inscrição pendente.")
            return

        for id_insc, nome, matricula, modalidade, id_mod in pendentes:
            aprovados = inscricao_repo.contar_aprovados(id_mod)
            vagas_max = modalidade_repo.buscar_vagas(id_mod)

            # 🔒 BLOQUEIO TOTAL SE LOTOU
            if aprovados >= vagas_max:
                modalidade_repo.encerrar(id_mod)
                inscricao_repo.remover_pendentes_da_modalidade(id_mod)
                st.rerun()

            st.markdown("----")
            st.write(f"👤 **Aluno:** {nome}")
            st.write(f"🆔 **Matrícula:** {matricula}")
            st.write(f"🏅 **Modalidade:** {modalidade}")

            c1, c2 = st.columns(2)

            with c1:
                if st.button("✅ Aprovar", key=f"ap_{id_insc}"):

                    inscricao_repo.aprovar(id_insc)
                    aprovados += 1

                    notificacao_repo.criar(
                        f"Você foi aprovado na modalidade {modalidade}",
                        matricula,
                        1
                    )

                    # SE LOTOU APÓS APROVAR
                    if aprovados >= vagas_max:
                        modalidade_repo.encerrar(id_mod)
                        inscricao_repo.remover_pendentes_da_modalidade(id_mod)

                    st.rerun()

            with c2:
                if st.button("❌ Recusar", key=f"re_{id_insc}"):
                    inscricao_repo.recusar(id_insc)
                    st.rerun()


def logout():
    st.session_state.page = "login"
    st.session_state.menu_admin = "postagens"

import streamlit as st
import time
import base64
from dao.postagem_repository import PostagemRepository
from dao.modalidade_repository import ModalidadeRepository
from dao.inscricao_repository import InscricaoRepository
from dao.notificacao_repository import NotificacaoRepository

def processar_imagem(image_file):
    if image_file is not None:
        return base64.b64encode(image_file.getvalue()).decode('utf-8')
    return None

def servidor_dashboard(db):
   
    postagem_repo = PostagemRepository(db)
    modalidade_repo = ModalidadeRepository(db)
    inscricao_repo = InscricaoRepository(db)
    notificacao_repo = NotificacaoRepository(db)

  
    with st.sidebar:
        st.header("🛠️ Admin IFSport")
        st.write("Bem-vindo, Servidor.")
        
        # Menu de Navegação usando Radio Button estilizado
        menu_opcao = st.radio(
            "Navegação",
            ["Dashboard", "Postagens", "Modalidades", "Aprovações"],
            index=0
        )
        
        st.divider()
        if st.button("🚪 Sair do Sistema", type="primary", use_container_width=True):
            logout()

    
    if menu_opcao == "Dashboard":
        st.title("📊 Visão Geral")
        
        # Métricas rápidas
        col1, col2, col3 = st.columns(3)
        total_pendentes = len(inscricao_repo.listar_pendentes())
        total_posts = len(postagem_repo.listar())
        total_mods = len(modalidade_repo.listar_todas())
        
        col1.metric("Solicitações Pendentes", total_pendentes, delta_color="inverse")
        col2.metric("Modalidades Ativas", total_mods)
        col3.metric("Postagens no Feed", total_posts)
        
        st.info("Selecione uma opção no menu lateral para gerenciar o sistema.")

    elif menu_opcao == "Postagens":
        st.title("📝 Gerenciar Notícias")
        
        with st.expander("➕ Criar Nova Postagem", expanded=False):
            with st.form("form_post"):
                titulo = st.text_input("Título da Postagem")
                conteudo = st.text_area("Conteúdo da Mensagem", height=150)
                
                # NOVO CAMPO: Upload de imagem
                arquivo_img = st.file_uploader("Adicionar Imagem (Opcional)", type=['png', 'jpg', 'jpeg'])

                submitted = st.form_submit_button("Publicar Agora")
                
                if submitted and titulo and conteudo:
                    # Converte a imagem para texto Base64
                    imagem_b64 = processar_imagem(arquivo_img)

                    postagem_repo.criar(titulo, conteudo, imagem_b64, 1) # Passa a imagem convertida
                    
                    st.toast("Postagem publicada com sucesso!", icon="✅")
                    time.sleep(1)
                    st.rerun()
        
        st.markdown("### 📰 Feed Atual")
        postagens = postagem_repo.listar()
        
        if not postagens:
            st.warning("Nenhuma postagem encontrada.")
            
        for id_post, titulo, conteudo, *_ in postagens:
            # Container visual (Card)
            with st.container(border=True):
                c_texto, c_btn = st.columns([5, 1])
                with c_texto:
                    st.subheader(titulo)
                    st.write(conteudo)
                with c_btn:
                    st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
                    if st.button("🗑️", key=f"del_post_{id_post}", help="Excluir Postagem", type="primary"):
                        postagem_repo.excluir(id_post)
                        st.toast("Postagem removida!", icon="🗑️")
                        time.sleep(0.5)
                        st.rerun()

   
    elif menu_opcao == "Modalidades":
        st.title("🏅 Gestão de Modalidades")
        
        with st.expander("➕ Nova Modalidade", expanded=False):
            with st.form("form_mod"):
                c1, c2 = st.columns([3, 1])
                nome = c1.text_input("Nome do Esporte")
                vagas_max = c2.number_input("Qtd. Vagas", min_value=1, value=20, step=1)
                
                if st.form_submit_button("Criar Modalidade"):
                    modalidade_repo.criar(nome, vagas_max)
                    st.toast(f"Modalidade {nome} criada!", icon="✅")
                    time.sleep(1)
                    st.rerun()

        st.markdown("### Monitoramento de Vagas")
        modalidades = modalidade_repo.listar_todas()
        
        for id_mod, nome, vagas_max in modalidades:
            aprovados = inscricao_repo.contar_aprovados(id_mod)
            lista_aprovados = inscricao_repo.listar_aprovados_por_modalidade(id_mod)
            
            # Cálculo de progresso (0.0 a 1.0)
            progresso = min(aprovados / vagas_max, 1.0)
            
            with st.container(border=True):
                # Cabeçalho do Card
                top_c1, top_c2, top_c3 = st.columns([3, 2, 1])
                top_c1.markdown(f"### {nome}")
                top_c2.caption(f"Lotação: {aprovados}/{vagas_max}")
                
                # Barra de progresso visual
                st.progress(progresso)
                
                if aprovados >= vagas_max:
                    st.error("🔒 LOTADO - Inscrições Fechadas")
                
                # Detalhes (Lista de alunos) 
                with st.expander(f"Ver Lista de Alunos ({aprovados})"):
                    if not lista_aprovados:
                        st.info("Nenhum aluno aprovado ainda.")
                    for aluno, matricula in lista_aprovados:
                        st.text(f"• {aluno} ({matricula})")
                
                if st.button("Excluir Modalidade", key=f"del_mod_{id_mod}"):
                    modalidade_repo.excluir(id_mod)
                    st.rerun()

    
    elif menu_opcao == "Aprovações":
        st.title("✅ Solicitações Pendentes")
        
        pendentes = inscricao_repo.listar_pendentes()
        
        if not pendentes:
            st.success("Tudo limpo! Nenhuma pendência no momento. 🎉")
            return

        # Layout em Grid para as pendências
        for id_insc, nome_aluno, matricula, nome_modalidade, id_mod in pendentes:
            with st.container(border=True):
                col_info, col_actions = st.columns([3, 2])
                
                with col_info:
                    st.markdown(f"**Aluno:** {nome_aluno}")
                    st.caption(f"Matrícula: {matricula}")
                    st.markdown(f"Solicitando: **{nome_modalidade}**")
                
                with col_actions:
                    bt_col1, bt_col2 = st.columns(2)
                    
                    if bt_col1.button("Aprovar", key=f"ap_{id_insc}", type="primary", use_container_width=True):
                        # LÓGICA DE APROVAÇÃO
                        vagas_totais = modalidade_repo.buscar_vagas(id_mod)
                        qtd_aprovados = inscricao_repo.contar_aprovados(id_mod)
                        
                        if qtd_aprovados >= vagas_totais:
                            st.error("Erro: Vagas esgotadas nesta modalidade!")
                        else:
                            inscricao_repo.aprovar(id_insc)
                            notificacao_repo.criar(f"Sua inscrição em {nome_modalidade} foi aprovada!", matricula, 1)
                            st.toast(f"{nome_aluno} aprovado!", icon="✅")
                            
                            # Verifica se lotou APÓS aprovar
                            if (qtd_aprovados + 1) >= vagas_totais:
                                modalidade_repo.encerrar(id_mod)
                                inscricao_repo.remover_pendentes_da_modalidade(id_mod)
                                st.warning(f"A modalidade {nome_modalidade} lotou e foi encerrada.")
                            
                            time.sleep(1)
                            st.rerun()
                            
                    if bt_col2.button("Recusar", key=f"rec_{id_insc}", use_container_width=True):
                        inscricao_repo.recusar(id_insc)
                        notificacao_repo.criar(f"Sua inscrição em {nome_modalidade} foi recusada.", matricula, 1)
                        st.toast("Solicitação recusada.", icon="❌")
                        time.sleep(0.5)
                        st.rerun()

def logout():
    st.session_state.aluno_logado = None
    st.session_state.servidor_logado = None
    st.session_state.page = "login"
    st.rerun()
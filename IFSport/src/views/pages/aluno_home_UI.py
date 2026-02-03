import streamlit as st
import time
import base64
from dao.postagem_repository import PostagemRepository
from dao.like_repository import LikeRepository
from dao.modalidade_repository import ModalidadeRepository
from dao.inscricao_repository import InscricaoRepository
from dao.aluno_repository import AlunoRepository
from dao.comentario_repository import ComentarioRepository 
from templates.styles import carregar_estilos


def renderizar_comentario_bonito(nome, texto, data):
    # Gera avatar com as iniciais
    nome_url = nome.replace(" ", "+")
    avatar_url = f"https://ui-avatars.com/api/?name={nome_url}&background=random&color=fff&size=64"

    html = f"""
    <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px;">
        <img src="{avatar_url}" style="width: 38px; height: 38px; border-radius: 50%; border: 1px solid #e0e0e0;">
        <div style="background-color: #f0f2f6; padding: 10px 14px; border-radius: 0px 15px 15px 15px; flex-grow: 1; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-weight: bold; color: #333; font-size: 13px;">{nome}</span>
                <span style="font-size: 10px; color: #888;">{data}</span>
            </div>
            <div style="color: #222; font-size: 14px; line-height: 1.4;">
                {texto}
            </div>
        </div>
    </div>
    """
    return html

def aluno_dashboard(db):
    # INICIALIZAÇÃO 
    postagem_repo = PostagemRepository(db)
    like_repo = LikeRepository(db)
    modalidade_repo = ModalidadeRepository(db)
    inscricao_repo = InscricaoRepository(db)
    aluno_repo = AlunoRepository(db)
    comentario_repo = ComentarioRepository(db)

    # Verificação de segurança
    if "aluno_logado" not in st.session_state or not st.session_state.aluno_logado:
        st.error("Sessão expirada. Faça login novamente.")
        st.stop()
        
    aluno_id_sessao, aluno_nome_sessao = st.session_state.aluno_logado

    #BUSCA DE DADOS REAIS 
    dados_completos = aluno_repo.buscar_por_id(aluno_id_sessao)
    
    if dados_completos:
        real_nome = dados_completos[0]
        real_email = dados_completos[1]
        real_matricula = dados_completos[2]
        real_curso = dados_completos[3]
    else:
        real_nome = aluno_nome_sessao
        real_email = "Não informado"
        real_matricula = "000000"
        real_curso = "Geral"

    #CABEÇALHO SUPERIOR
    col_logo, col_logout = st.columns([8, 1])
    
    with col_logo:
        st.title(f"Olá, {real_nome.split()[0]} 👋") 
    
    with col_logout:
        if st.button("Sair", type="primary", help="Sair do sistema"):
            logout()

    #BARRA DE NAVEGAÇÃO
    tab_feed, tab_inscricoes, tab_perfil = st.tabs(["📰 Feed de Notícias", "🏅 Inscrições", "👤 Meu Perfil"])

    #FEED
    with tab_feed:
        st.markdown("### Últimas Atualizações")
        postagens = postagem_repo.listar()
        
        if not postagens:
            st.info("Nenhuma postagem recente.")
        
        # Loop das postagens
        for id_post, titulo, conteudo, imagem_b64, data_post, _ in postagens:
            
            curtidas = like_repo.contar(id_post)
            curtiu = like_repo.usuario_curtiu(id_post, aluno_id_sessao)
            
            # Conta quantos comentários existem
            qtd_comentarios = comentario_repo.contar(id_post)

            with st.container(border=True):
                #Imagem e Conteúdo
                if imagem_b64:
                    try:
                        st.image(base64.b64decode(imagem_b64), width=350)
                    except:
                        st.error("Erro ao carregar imagem")

                st.subheader(titulo)
                st.write(conteudo)
                st.caption(f"📅 {data_post}")
                st.markdown("---")
                
                #Área de Likes e Info
                c1, c2 = st.columns([1, 3])
                with c1:
                    label_btn = "Descurtir" if curtiu else "Curtir"
                    tipo_btn = "primary" if curtiu else "secondary"
                    icon_btn = "❤️" if curtiu else "🤍"
                    
                    if st.button(f"{icon_btn} {label_btn}", key=f"like_btn_{id_post}", type=tipo_btn, use_container_width=True):
                        if curtiu:
                            like_repo.remover(aluno_id_sessao, id_post) 
                        else:
                            like_repo.adicionar(id_post, aluno_id_sessao) 
                        st.rerun()
                
                with c2:
                    st.caption(f"👍 {curtidas} curtidas • 💬 {qtd_comentarios} comentários")

                #ÁREA DE COMENTÁRIOS
                with st.expander(f"Ver discussão ({qtd_comentarios})"):
                    # Lista comentários existentes
                    lista_coments = comentario_repo.listar_por_postagem(id_post)
                    
                    if not lista_coments:
                        st.caption("Seja o primeiro a comentar!")
                    else:
                        st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
                        for autor_coment, texto_coment, data_coment in lista_coments:
                            # AQUI ESTÁ A MUDANÇA VISUAL:
                            st.markdown(renderizar_comentario_bonito(autor_coment, texto_coment, data_coment), unsafe_allow_html=True)

                st.markdown("---")
                
                # FORMULÁRIO MINIMALISTA
                # clear_on_submit=True limpa o texto automaticamente ao enviar
                with st.form(key=f"form_coment_{id_post}", clear_on_submit=True):
                    
                    # Colunas: Input grande na esquerda, Botão pequeno na direita
                    c_input, c_btn = st.columns([6, 1], gap="small")
                    
                    with c_input:
                        # label_visibility="collapsed" esconde o título "Comentar"
                        novo_texto = st.text_input(
                            label="Comentar", 
                            placeholder="Escreva um comentário...", 
                            label_visibility="collapsed"
                        )
                    
                    with c_btn:
                        # Botão apenas com ícone, sem cor de fundo (estilo definido no CSS)
                        enviou = st.form_submit_button("➤", use_container_width=True)
                    
                    if enviou and novo_texto:
                        sucesso = comentario_repo.adicionar(aluno_id_sessao, id_post, novo_texto)
                        if sucesso:
                            # Feedback discreto (toast em vez de success box grande)
                            st.toast("Comentário enviado!", icon="✅")
                            time.sleep(0.5)
                            st.rerun()

    #INSCRIÇÕES
    with tab_inscricoes:
        c_disp, c_minhas = st.columns(2)
        
        inscricoes_aluno = inscricao_repo.buscar_por_aluno(aluno_id_sessao)
        nomes_inscritos = {nome for nome, _ in inscricoes_aluno}

        #Disponíveis
        with c_disp:
            st.markdown("#### 🎯 Modalidades Abertas")
            modalidades = modalidade_repo.listar_disponiveis()
            
            for id_mod, nome, vagas in modalidades:
                with st.container(border=True):
                    st.markdown(f"**{nome}**")
                    st.caption(f"Vagas: {vagas}")
                    
                    if nome in nomes_inscritos:
                        st.success("Já inscrito ✅")
                    elif vagas > 0:
                        if st.button("Inscrever-se", key=f"ins_{id_mod}", use_container_width=True):
                            inscricao_repo.solicitar(aluno_id_sessao, id_mod)
                            st.toast(f"Inscrição solicitada para {nome}!", icon="✅")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.warning("Esgotado ❌")

        with c_minhas:
            st.markdown("#### 📋 Minhas Solicitações")
            if not inscricoes_aluno:
                st.info("Nenhuma inscrição ativa.")
            
            for nome_mod, status in inscricoes_aluno:
                cor_status = "gray"
                if status == "PENDENTE": cor_status = "orange"
                elif status == "APROVADO": cor_status = "green"
                elif status == "RECUSADO": cor_status = "red"
                
                with st.container(border=True):
                    col_txt, col_badge = st.columns([3, 1])
                    with col_txt:
                        st.write(f"**{nome_mod}**")
                    with col_badge:
                        st.markdown(f":{cor_status}[{status}]")

    #PERFIL
    with tab_perfil:
        st.markdown("### Configurações da Conta")
        
        with st.container(border=True):
            col_avatar, col_info = st.columns([2, 6], gap="medium")
            
            with col_avatar:
                nome_fmt = real_nome.replace(" ", "+")
                st.image(f"https://ui-avatars.com/api/?name={nome_fmt}&background=0D8ABC&color=fff&size=256", width=180)
            
            with col_info:
                # Usei um espaçamento vertical para alinhar o texto com o meio da foto maior
                st.markdown("<div style='padding-top: 20px;'></div>", unsafe_allow_html=True)
                st.markdown(f"## {real_nome}")
                st.markdown(f"**Matrícula:** `{real_matricula}`")
                st.caption("Aluno Regular • IFSport")
        
        st.markdown("#### Dados Cadastrais")
        with st.container(border=True):
            st.text_input("Nome Completo", value=real_nome, disabled=True)
            st.text_input("E-mail Institucional", value=real_email, disabled=True)
            st.text_input("Curso", value=real_curso, disabled=True)

def logout():
    st.session_state.aluno_logado = None
    st.session_state.page = "login"
    st.rerun()
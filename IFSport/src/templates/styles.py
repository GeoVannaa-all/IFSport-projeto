import streamlit as st

def carregar_estilos():
    st.markdown("""
    <style>
        /* =============================================
           1. LAYOUT, ZOOM E RESPONSIVIDADE
           ============================================= */
        
        /* AUMENTA TUDO EM 10% */
        html {
            font-size: 110% !important;
        }

        /* .block-container é a classe mestre do Streamlit */
        .block-container {
            max-width: 1200px !important; /* Aumentado para 1200px (Bem mais largo) */
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
            margin: auto !important;
        }

        /* Fundo geral */
        .stApp {
            background-color: #0e1117;
        }
        
        /* Fontes mais limpas */
        p, .stMarkdown, div, h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif !important;
        }

        /* =============================================
           2. ESTILIZAÇÃO DOS CONTAINERS (CARDS)
           ============================================= */
        
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #161b22;
            border: 1px solid #30363d !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px !important; /* Aumentei um pouco o padding interno */
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
             border-color: #8b949e !important;
        }

        /* =============================================
           3. TIPOGRAFIA E ELEMENTOS
           ============================================= */
        
        h1, h2, h3 {
            color: #ffffff !important;
        }

        p, div, span {
            color: #c9d1d9;
        }

        div.stButton > button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            height: auto !important;
            padding-top: 0.6rem !important;
            padding-bottom: 0.6rem !important;
        }
        
        /* Remove a borda padrão do st.form para ficar invisível */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0px !important;
        }

        /* Estiliza o campo de input para ser mais discreto */
        div[data-testid="stForm"] input {
            background-color: #0d1117 !important; /* Mais escuro que o card */
            border: 1px solid #30363d !important;
            color: #e6edf3 !important;
            border-radius: 6px !important;
        }
        
        div[data-testid="stForm"] input:focus {
            border-color: #58a6ff !important;
            box-shadow: none !important;
        }

        /* Botão de enviar minimalista (dentro do form) */
        div[data-testid="stForm"] button {
            background-color: transparent !important;
            border: 1px solid #30363d !important;
            color: #8b949e !important;
            font-size: 14px !important;
            padding: 0.4rem 1rem !important;
            margin-top: 2px !important; /* Alinhamento fino com o input */
        }

        div[data-testid="stForm"] button:hover {
            border-color: #8b949e !important;
            color: #ffffff !important;
            background-color: #21262d !important;
        }

        /* Remove o espaço extra que o Streamlit coloca nos forms */
        div[data-testid="stForm"] .stElementContainer {
            margin-bottom: 0px !important;
        }
    </style>
    """, unsafe_allow_html=True)
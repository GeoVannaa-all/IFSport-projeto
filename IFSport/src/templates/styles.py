import streamlit as st

def carregar_estilos():
    st.markdown("""
    <style>
    body {
        background-color: #f4f6f8;
    }

    .header-title {
        font-size: 26px;
        font-weight: bold;
        color: #006400;
    }

    .main-container {
        max-width: 1000px;
        margin: auto;
        padding-top: 20px;
    }

    .card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 18px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }
    </style>
    """, unsafe_allow_html=True)

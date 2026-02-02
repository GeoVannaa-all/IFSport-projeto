import streamlit as st

def carregar_estilos():
    st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }

    .header-title {
        font-size: 28px;
        font-weight: bold;
        color: #00c853;
    }

    .main-container {
        max-width: 900px;
        margin: auto;
        padding-top: 30px;
    }

    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.35);
        transition: 0.2s ease;
    }

    .card:hover {
        box-shadow: 0 6px 18px rgba(0,0,0,0.45);
        transform: scale(1.01);
    }

    .card h3 {
        margin-bottom: 6px;
        color: #ffffff;
    }

    .card p {
        color: #c9d1d9;
    }

    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 12px;
        font-size: 14px;
        color: #9da5b4;
    }
                
    .feed-container {
    border: 1px solid #30363d;
    border-radius: 18px;
    padding: 25px;
    background-color: #0d1117;
    margin-top: 25px;
    }

    .feed-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 18px;
        color: #ffffff;
        border-bottom: 1px solid #30363d;
        padding-bottom: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

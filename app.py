import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔")

# CSS PERSONALIZADO (Verde Menta)
st.markdown("""
    <style>
    .stApp { background-color: #E8F5E9; color: #1B5E20; }
    .stButton>button { 
        background-color: #2E7D32; color: white; 
        border-radius: 8px; width: 100%; font-weight: bold; 
    }
    .stCheckbox, .stTextInput, .stSelectbox {
        background-color: #FFFFFF; padding: 10px; 
        border-radius: 10px; border: 1px solid #C8E6C9;
    }
    h1, h2, h3 { color: #1B5E20; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 Trailer do Alan")

# --- 1. CONFIGURAÇÃO DO CARDÁPIO ---
cardapio = {
    "Selecione seu lanche...": {"preco": 0.00, "itens": "Escolha uma opção abaixo"},
    "X-Burger": {"preco": 20.00, "itens": "Pão, Carne, Queijo"},
    "X-Salada": {"preco": 22.00, "itens": "Pão, Carne, Queijo, Alface, Tomate"},
    "X-Tudo": {"preco": 28.00, "itens": "Pão, Carne, Queijo, Ovo, Bacon, Salada, Milho"},
    "Combo Alan": {"preco": 35

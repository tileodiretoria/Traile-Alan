import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔")

# ⚠️ COLOQUE O LINK DA SUA PLANILHA AQUI:
url_planilha = "https://docs.google.com/spreadsheets/d/1NOZvZcbmx0BgXdsXoeDGkonwusjJaqNFDnN86LGQWfw/edit?gid=0#gid=0"

# Conectando com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# --- CSS PERSONALIZADO (Verde Menta) ---
st.markdown("""
    <style>
    .stApp { background-color: #E8F5E9; color: #1B5E20; }
    .stButton>button { background-color: #2E7D32; color: white; border-radius: 8px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍔 Trailer do Alan")

# --- CARDÁPIO ---
cardapio = {
    "Selecione...": {"preco": 0.00},
    "X-Burger": {"preco": 20.00},
    "X-Salada": {"preco": 22.00},
    "X-Bacon": {"preco": 25.00},
    "X-Tudo": {"preco": 28.00}
}

# --- DADOS DO CLIENTE ---
nome = st.text_input("Nome do Cliente")
endereco = st.text_input("Endereço de Entrega")

# --- PEDIDO ---
escolha_lanche = st.selectbox("Escolha seu lanche:", list(cardapio.keys()))
valor_lanche = cardapio[escolha_lanche]["preco"]

bebidas = {"Nenhuma": 0, "Refri Lata": 5, "Refri 2L": 15}
escolha_bebida = st.selectbox("Bebida:", list(bebidas.keys()))
valor_bebida = bebidas[escolha_bebida]

total = valor_lanche + valor_bebida
st.subheader(f"Total: R$ {total:.2f}")

# --- BOTÃO SALVAR ---
if st.button("✅ FINALIZAR E SALVAR PEDIDO"):
    if escolha_lanche != "Selecione..." and nome:
        # Preparar dados
        novo_pedido = pd.DataFrame([{
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Nome": nome,
            "Endereco": endereco,
            "Lanche": escolha_lanche,
            "Bebida": escolha_bebida,
            "Total": total
        }])

        # Salvar na Planilha
        try:
            dados_antigos = conn.read(spreadsheet=url_planilha)
            tabela_nova = pd.concat([dados_antigos, novo_pedido], ignore_index=True)
            conn.update(spreadsheet=url_planilha, data=tabela_nova)
            st.success("📊 Pedido registrado na planilha com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar na planilha: {e}")
            
        # Link do WhatsApp
        texto_wa = f"Novo Pedido de {nome}: {escolha_lanche} e {escolha_bebida}. Total: R${total}".replace(" ", "%20")
        st.link_button("Avisar Alan no WhatsApp", f"https://wa.me/5511999999999?text={texto_wa}")
    else:
        st.warning("Por favor, preencha o nome e escolha um lanche.")

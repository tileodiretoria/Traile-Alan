import streamlit as st
import pandas as pd
import os

# --- CONFIGURAÇÃO INICIAL ---
st.title("🍔 Trailer do Alan - Sistema de Vendas")

# --- CADASTRO ---
st.sidebar.header("👤 Dados do Cliente")
nome = st.sidebar.text_input("Nome")
endereco = st.sidebar.text_input("Endereço")
telefone = st.sidebar.text_input("Telefone")

# --- PEDIDO ---
st.header("🛒 Cardápio")
lanches = {"X-Burger (PÃO, HAMBURGUER E QUEIJO)": 20.0, "X-Salada EEEE": 22.0, "X-BACON": 25.0}
escolha = st.selectbox("Selecione o lanche:", list(lanches.keys()))

st.subheader("➕ Adicionais")
add_bacon = st.checkbox("Bacon (+ R$ 3,00)")
add_queijo = st.checkbox("Queijo (+ R$ 2,50)")
add_milho = st.checkbox("milho (+R$ 1,00)")
add_batatapalha = st.checkbox("batata palha (+R$ 1,00)")

# Cálculo do Total
total = lanches[escolha]
if add_bacon: total += 3.0
if add_queijo: total += 2.5
if add_milho: total += 1.0
if add_batatapalha: total += 1.0

st.markdown(f"### 💰 Total: **R$ {total:.2f}**")

# --- BOTÃO FINALIZAR E SALVAR ---
if st.button("Finalizar Pedido"):
    if nome and endereco and telefone:
        # Criamos um "dicionário" com os dados que você escolheu
        novo_pedido = {
            "Nome": [nome],
            "Endereço": [endereco],
            "Telefone": [telefone],
            "Total": [total]
        }
        df = pd.DataFrame(novo_pedido)

        # Lógica: Se o arquivo não existe, cria com cabeçalho. Se existe, adiciona abaixo.
        if not os.path.isfile("pedidos.csv"):
            df.to_csv("pedidos.csv", index=False, sep=";", encoding="utf-8-sig")
        else:
            df.to_csv("pedidos.csv", mode='a', index=False, header=False, sep=";", encoding="utf-8-sig")
        
        st.balloons()
        st.success("✅ Pedido gravado na planilha com sucesso!")
    else:
        st.error("⚠️ Preencha todos os campos do cadastro!")
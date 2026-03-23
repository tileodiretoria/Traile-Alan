import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔", layout="centered")

# --- CSS (Azul e Branco conforme as imagens) ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 110px; font-weight: bold; border: none; font-size: 14px; margin-bottom: 10px; white-space: pre-wrap;
    }
    .stButton>button:hover { background-color: #0077b6; transform: scale(1.02); }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar(nome, preco, ing):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ing})
    st.toast(f"✅ {nome} adicionado!")

st.title("🍔 Trailer do Alan")

# --- ABAS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

with tab1:
    # --- CATEGORIA CARNE ---
    with st.expander("✨ Opções de Hambúrguer de Carne"):
        pb = 10.0
        c1, c2 = st.columns(2)
        # Itens de Carne (Nome original conforme solicitado antes)
        lanches_carne = [
            {"n": "Hambúrguer", "p": pb, "ing": "Pão, Carne, Alface e Tomate"},
            {"n": "X-Burger", "p": pb+5, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
            {"n": "X-Egg", "p": pb+8, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
            {"n": "X-Bacon", "p": pb+10, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
            {"n": "X-Presunto", "p": pb+7, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"},
            {"n": "X-Bacon Presunto", "p": pb+13, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"}
        ]
        for i, l in enumerate(lanches_carne):
            col = c1 if i % 2 == 0 else c2
            if col.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"carne_{i}"):
                adicionar(f"{l['n']} Carne", l['p'], l['ing'])

    # --- CATEGORIA FRANGO (Ajustada conforme sua última orientação) ---
    with st.expander("✨ Opções de Hambúrguer de Frango"):
        tipo = "Hambúrguer de Frango" # Nome corrigido conforme pedido
        pb = 12.0
        c1, c2 = st.columns(2)
        lanches_frango = [
            {"n": f"{tipo}", "p": pb, "ing": f"Pão, {tipo}, Alface e Tomate"},
            {"n": f"X-Burger {tipo}", "p": pb+5, "ing": f"Pão, {tipo}, Queijo, Alface e Tomate"},
            {"n": f"X-Egg {tipo}", "p": pb+8, "ing": f"Pão, {tipo}, Queijo, Ovo, Alface e Tomate"},
            {"n": f"X-Bacon {tipo}", "p": pb+10, "ing": f"Pão, {tipo}, Queijo, Bacon, Alface e Tomate"},
            {"n": f"X-Presunto {tipo}", "p": pb+7, "ing": f"Pão, {tipo}, Queijo, Presunto, Alface e Tomate"},
            {"n": f"X-Bacon Presunto {tipo}", "p": pb+13, "ing": f"Pão, {tipo}, Queijo, Bacon, Presunto, Alface e Tomate"}
        ]
        for i, l in enumerate(lanches_frango):
            col = c1 if i % 2 == 0 else c2
            if col.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"frango_{i}"):
                adicionar(l['n'], l['p'], l['ing'])

with tab5:
    st.subheader("🏁 Dados para Entrega")
    nome = st.text_input("Seu Nome:")
    end = st.text_input("Endereço:")
    obs = st.text_area("Observações:")
    
    if st.button("🟢 ENVIAR PARA WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            txt_itens = "\n".join([f"* {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            total = sum(i['preco'] for i in st.session_state.carrinho)
            msg = f"*NOVO PEDIDO*\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*\n{txt_itens}\n\n*Total:* R$ {total:.2f}\n*Obs:* {obs}"
            # Coloque o número do Alan aqui:
            st.link_button("Abrir WhatsApp", f"https://wa.me/5511999999999?text={msg.replace(' ', '%20').replace('\n', '%0A')}")

if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total: R$ {sum(i["preco"] for i in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

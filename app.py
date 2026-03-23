import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan", page_icon="🍔", layout="centered")

# --- CSS PERSONALIZADO (Azul Claro e Branco Neve) ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; } /* Branco Neve / Azul Alice */
    .main-title { color: #0077b6; font-size: 38px; font-weight: bold; text-align: center; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 110px; font-weight: bold; border: none; transition: 0.3s;
        font-size: 14px; margin-bottom: 10px; white-space: pre-wrap;
    }
    .stButton>button:hover { background-color: #0077b6; transform: scale(1.02); }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🍔 Trailer do Alan</p>', unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar(nome, preco, ingredientes):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ingredientes})
    st.toast(f"✅ {nome} adicionado!")

# --- ABAS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

with tab1:
    # Categoria específica de Frango com a nomenclatura solicitada
    with st.expander("✨ Opções de Hambúrguer de Frango"):
        tipo_exibicao = "Hambúrguer de Frango" # Nome solicitado para os botões
        pb = 12.0 # Preço base de frango
        col1, col2 = st.columns(2)
        
        lanches_frango = [
            {"n": f"{tipo_exibicao}", "p": pb, "ing": f"Pão, {tipo_exibicao}, Alface e Tomate"},
            {"n": f"X-Burger {tipo_exibicao}", "p": pb+5, "ing": f"Pão, {tipo_exibicao}, Queijo, Alface e Tomate"},
            {"n": f"X-Egg {tipo_exibicao}", "p": pb+8, "ing": f"Pão, {tipo_exibicao}, Queijo, Ovo, Alface e Tomate"},
            {"n": f"X-Bacon {tipo_exibicao}", "p": pb+10, "ing": f"Pão, {tipo_exibicao}, Queijo, Bacon, Alface e Tomate"},
            {"n": f"X-Presunto {tipo_exibicao}", "p": pb+7, "ing": f"Pão, {tipo_exibicao}, Queijo, Presunto, Alface e Tomate"},
            {"n": f"X-Bacon Presunto {tipo_exibicao}", "p": pb+13, "ing": f"Pão, {tipo_exibicao}, Queijo, Bacon, Presunto, Alface e Tomate"},
            {"n": f"X-Egg Bacon Presunto {tipo_exibicao}", "p": pb+16, "ing": f"Pão, {tipo_exibicao}, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
        ]

        for i, l in enumerate(lanches_frango):
            col_target = col1 if i % 2 == 0 else col2
            btn_label = f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})"
            if col_target.button(btn_label, key=f"frango_{i}"):
                adicionar(l['n'], l['p'], l['ing'])

    # Outras categorias (Carne, Lombo, Picanha) seguem aqui...
    st.info("As demais categorias (Carne, Lombo e Picanha) aparecem abaixo desta seção.")

# --- ABA FINALIZAR (WhatsApp) ---
with tab5:
    st.subheader("🏁 Finalize seu Pedido")
    nome = st.text_input("Seu Nome:")
    end = st.text_input("Endereço:")
    
    total_final = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO"):
        if nome and end and st.session_state.carrinho:
            itens_texto = "\n".join([f"* {i['item']}" for i in st.session_state.carrinho])
            mensagem = f"*PEDIDO - ALAN*\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*\n{itens_texto}\n\n*TOTAL: R$ {total_final:.2f}*"
            link = f"https://wa.me/5511999999999?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Confirmar no WhatsApp", link)

if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total: R$ {sum(item["preco"] for item in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

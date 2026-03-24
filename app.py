import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (AUTONOMIA TOTAL DO LEO)
# =========================================================

# 1. TÍTULOS DAS 5 ABAS (Mude o texto entre aspas)
TITULO_ABA_1 = "Hambúrguer Simples"
TITULO_ABA_2 = "Hambúrguer de Frango"
TITULO_ABA_3 = "Hambúrguer de Lombo"
TITULO_ABA_4 = "Hambúrguer de Picanha"
TITULO_ABA_5 = "Filé de Frango"

# 2. CARDÁPIO DETALHADO (Mude nomes, preços e ingredientes aqui)
# Basta alterar o que está entre aspas ou o número do preço.
ITENS_CARDAPIO = {
    TITULO_ABA_1: [
        {"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"},
        {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
        {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    TITULO_ABA_2: [
        {"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"},
        {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"},
        {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    TITULO_ABA_3: [
        {"n": "Hambúrguer Lombo", "p": 14.00, "ing": "Pão, Lombo, Alface e Tomate"},
        {"n": "X-Burger Lombo", "p": 19.00, "ing": "Pão, Lombo, Queijo, Alface e Tomate"},
        {"n": "X-Egg Lombo", "p": 22.00, "ing": "Pão, Lombo, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Lombo", "p": 24.00, "ing": "Pão, Lombo, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Lombo", "p": 21.00, "ing": "Pão, Lombo, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Lombo", "p": 27.00, "ing": "Pão, Lombo, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Lombo", "p": 30.00, "ing": "Pão, Lombo, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    TITULO_ABA_4: [
        {"n": "Hambúrguer Picanha", "p": 18.00, "ing": "Pão, Picanha, Alface e Tomate"},
        {"n": "X-Burger Picanha", "p": 23.00, "ing": "Pão, Picanha, Queijo, Alface e Tomate"},
        {"n": "X-Egg Picanha", "p": 26.00, "ing": "Pão, Picanha, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Picanha", "p": 28.00, "ing": "Pão, Picanha, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Picanha", "p": 25.00, "ing": "Pão, Picanha, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Picanha", "p": 31.00, "ing": "Pão, Picanha, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Picanha", "p": 34.00, "ing": "Pão, Picanha, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    TITULO_ABA_5: [
        {"n": "Filé de Frango", "p": 15.00, "ing": "Pão, Filé, Alface e Tomate"},
        {"n": "X-Burger Filé", "p": 20.00, "ing": "Pão, Filé, Queijo, Alface e Tomate"},
        {"n": "X-Egg Filé", "p": 23.00, "ing": "Pão, Filé, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Filé", "p": 25.00, "ing": "Pão, Filé, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Filé", "p": 22.00, "ing": "Pão, Filé, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Filé", "p": 28.00, "ing": "Pão, Filé, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Filé", "p": 31.00, "ing": "Pão, Filé, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ]
}

# 3. ADICIONAIS, BEBIDAS E DOCES
ADICIONAIS = {"Queijo": 3.0, "Presunto": 3.0, "Ovo": 3.0, "Bacon": 5.0, "Milho": 2.0, "Batata": 4.0}
BEBIDAS = {"Lata": 5.0, "600ml": 8.0, "1 Litro": 10.0, "2 Litros": 15.0}
DOCES = {"Brigadeiro": 4.0, "Beijinho": 4.0, "Doce Amendoim": 3.0}

# 4. CONFIGURAÇÃO WHATSAPP
WHATSAPP_NUMERO = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE (NÃO MEXER)
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 110px; font-weight: bold; font-size: 14px; margin-bottom: 10px;
    }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def add(n, p, i):
    st.session_state.carrinho.append({"item": n, "preco": p, "ing": i})
    st.toast(f"✅ {n} adicionado!")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

with tabs[0]:
    for titulo, lanches in ITENS_CARDAPIO.items():
        with st.expander(f"✨ Opções de {titulo}"):
            c1, c2 = st.columns(2)
            for idx, l in enumerate(lanches):
                col = c1 if idx % 2 == 0 else c2
                if col.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"{titulo}_{idx}"):
                    add(l['n'], l['p'], l['ing'])

with tabs[1]:
    c1, c2 = st.columns(2)
    for i, (item, preco) in enumerate(ADICIONAIS.items()):
        col = c1 if i % 2 == 0 else c2
        if col.button(f"{item}\n+ R$ {preco:.2f}"):
            add(f"Extra {item}", preco, "Adicional")

with tabs[2]:
    for item, preco in BEBIDAS.items():
        if st.button(f"🥤 {item} - R$ {preco:.2f}"):
            add(item, preco, "Bebida")

with tabs[3]:
    for item, preco in DOCES.items():
        if st.button(f"🍰 {item} - R$ {preco:.2f}"):
            add(item, preco, "Doce")

with tabs[4]:
    n_cli = st.text_input("Nome:")
    e_cli = st.text_input("Endereço:")
    t_cli = st.text_input("Telefone:")
    o_cli = st.text_area("Observações:")
    total = sum(i['preco'] for i in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO"):
        if n_cli and e_cli and st.session_state.carrinho:
            txt = f"*PEDIDO*\n*Cliente:* {n_cli}\n*End:* {e_cli}\n*Tel:* {t_cli}\n\n*ITENS:*\n"
            txt += "\n".join([f"- {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            txt += f"\n\n*OBS:* {o_cli}\n*TOTAL: R$ {total:.2f}*"
            st.link_button("Abrir WhatsApp ✅", f"https://wa.me/{WHATSAPP_NUMERO}?text={txt.replace(' ', '%20').replace('\n', '%0A')}")

if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total: R$ {sum(i["preco"] for i in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

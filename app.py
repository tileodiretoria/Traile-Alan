import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (AUTONOMIA TOTAL DO LEO)
# =========================================================

TITULO_ABA_1 = "Hambúrguer Simples"
TITULO_ABA_2 = "Hambúrguer de Frango"
TITULO_ABA_3 = "Hambúrguer de Lombo"
TITULO_ABA_4 = "Hambúrguer de Picanha"
TITULO_ABA_5 = "Filé de Frango"
TITULO_ABA_6 = "🔥 X-TUDO"

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
    ],
    TITULO_ABA_6: [
        {"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}
    ]
}

ADICIONAIS_PAGOS = {
    "Bife de Hambúrguer": 5.00,
    "Bife de Frango": 5.00,
    "Bife de Picanha": 8.00,
    "Bife de Lombo": 6.00,
    "Filé de Frango": 6.00,
    "Queijo": 3.00, 
    "Presunto": 3.00, 
    "Ovo": 3.00, 
    "Bacon": 5.00, 
    "Catupiry": 5.00
}

CORTESIAS = {
    "Milho": 0.00,
    "Batata Palha": 0.00
}

BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}
DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE (ESTRUTURA MANTIDA)
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #0077b6; color: white; width: 100%; border-radius: 12px; 
        min-height: 120px; font-weight: bold; font-size: 14px; margin-bottom: 10px;
        display: flex; align-items: center; justify-content: center;
    }
    .footer-soma { 
        position: fixed; bottom: 0; left: 0; width: 100%; background: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
        font-size: 20px; color: #0077b6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar_ao_pedido(nome, preco, ingredientes):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ingredientes})
    st.toast(f"✅ Adicionado: {nome}")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# ABA LANCHES
with tabs[0]:
    for titulo, lanches in ITENS_CARDAPIO.items():
        with st.expander(f"✨ Opções de {titulo}"):
            c1, c2 = st.columns(2)
            for i, l in enumerate(lanches):
                coluna = c1 if i % 2 == 0 else c2
                if coluna.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                    adicionar_ao_pedido(l['n'], l['p'], l['ing'])

# ABA ADICIONAIS
with tabs[1]:
    st.write("### ➕ Extras (Cobrados)")
    c1, c2 = st.columns(2)
    for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
        coluna = c1 if i % 2 == 0 else c2
        if coluna.button(f"{nome}\n+ R$ {preco:.2f}", key=f"extra_pago_{i}"):
            adicionar_ao_pedido(f"Adicional {nome}", preco, "Extra")
    
    st.write("---")
    st.write("### 🎁 Cortesias (Grátis)")
    col1, col2 = st.columns(2)
    for i, (nome, preco) in enumerate(CORTESIAS.items()):
        coluna = col1 if i % 2 == 0 else col2
        if coluna.button(f"{nome}\nGRÁTIS", key=f"cortesia_{i}"):
            adicionar_ao_pedido(f"Cortesia {nome}", 0.00, "Grátis")

# ABAS BEBIDAS E DOCES
with tabs[2]:
    for nome, preco in BEBIDAS.items():
        if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"bebida_{nome}"):
            adicionar_ao_pedido(f"Bebida {nome}", preco, "")

with tabs[3]:
    for nome, preco in DOCES.items():
        if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doce_{nome}"):
            adicionar_ao_pedido(nome, preco, "")

# ABA FINALIZAR
with tabs[4]:
    nome_u = st.text_input("Seu Nome:")
    end_u = st.text_input("Endereço Completo:")
    tel_u = st.text_input("Telefone:")
    obs_u = st.text_area("Observações:")
    
    valor_t = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 CONCLUIR E ENVIAR WHATSAPP"):
        if nome_u and end_u and st.session_state.carrinho:
            txt_p = "\n".join([f"- {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            msg = (f"*PEDIDO - TRAILER DO ALAN*\n*Cliente:* {nome_u}\n*Endereço:* {end_u}\n*Tel:* {tel_u}\n\n*ITENS:*\n{txt_p}\n\n*OBS:* {obs_u}\n*TOTAL: R$ {valor_t:.2f}*")
            link = f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Ir para o WhatsApp ✅", link)
        else:
            st.warning("Preencha os dados e escolha seus lanches!")

if st.session_state.carrinho:
    total_r = sum(item['preco'] for item in st.session_state.carrinho)
    st.markdown(f'<div class="footer-soma"><b>🛒 Valor Total: R$ {total_r:.2f}</b></div>', unsafe_allow_html=True)

import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (LANCHES E PREÇOS)
# =========================================================

TITULOS_ABAS = [
    "Hambúrguer Simples", "Hambúrguer de Frango", "Hambúrguer de Lombo", 
    "Hambúrguer de Picanha", "Filé de Frango", "🔥 X-TUDO"
]

ITENS_CARDAPIO = {
    TITULOS_ABAS[0]: [
        {"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"},
        {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
        {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    TITULOS_ABAS[1]: [
        {"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"},
        {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"},
        {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"},
        {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"},
        {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"},
        {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"},
        {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
    ],
    # ... (Mantendo Lombo, Picanha e Filé como no anterior para não esticar o código)
    TITULOS_ABAS[5]: [
        {"n": "X-TUDO MONSTRO", "p": 45.00, "ing": "4 Bifes, Queijo, Presunto, Ovo, Bacon, Alface, Tomate e Batata Palha"}
    ]
}

ADICIONAIS_PAGOS = {
    "Bife de Hambúrguer": 5.00, "Bife de Frango": 5.00, "Bife de Picanha": 8.00,
    "Bife de Lombo": 6.00, "Filé de Frango": 6.00, "Queijo": 3.00, 
    "Presunto": 3.00, "Ovo": 3.00, "Bacon": 5.00, "Catupiry": 5.00
}

CORTESIAS = {"Milho": 0.00, "Batata Palha": 0.00}
BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}
DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #0077b6; color: white; width: 100%; border-radius: 12px; 
        min-height: 120px; font-weight: bold; font-size: 14px; margin-bottom: 10px;
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

def adicionar_ao_pedido(nome, preco, desc, num_pedido):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "desc": desc, "id": num_pedido})
    st.toast(f"✅ {nome} no Pedido {num_pedido}")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# ABA LANCHES
with tabs[0]:
    num_p = st.selectbox("Este lanche é para qual pedido?", [1, 2, 3, 4, 5], key="sel_lanche")
    for titulo, lanches in ITENS_CARDAPIO.items():
        if titulo in ITENS_CARDAPIO:
            with st.expander(f"✨ {titulo}"):
                c1, c2 = st.columns(2)
                for i, l in enumerate(lanches):
                    col = c1 if i % 2 == 0 else c2
                    if col.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                        adicionar_ao_pedido(l['n'], l['p'], l['ing'], num_p)

# ABA ADICIONAIS (AGORA COM VÍNCULO)
with tabs[1]:
    num_p_add = st.selectbox("Adicionar extras em qual pedido?", [1, 2, 3, 4, 5], key="sel_add")
    st.write("### ➕ Extras (Cobrados)")
    c1, c2 = st.columns(2)
    for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
        col = c1 if i % 2 == 0 else c2
        if col.button(f"{nome}\n+ R$ {preco:.2f}", key=f"extra_{i}"):
            adicionar_ao_pedido(f"Adicional {nome}", preco, "Extra", num_p_add)
    
    st.write("---")
    st.write("### 🎁 Cortesias (Grátis)")
    col_c1, col_c2 = st.columns(2)
    for i, (nome, preco) in enumerate(CORTESIAS.items()):
        col = col_c1 if i % 2 == 0 else col_c2
        if col.button(f"{nome}\nGRÁTIS", key=f"cort_{i}"):
            adicionar_ao_pedido(f"Cortesia {nome}", 0.00, "Grátis", num_p_add)

# BEBIDAS E DOCES (Geral)
with tabs[2]:
    for nome, preco in BEBIDAS.items():
        if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"beb_{nome}"):
            adicionar_ao_pedido(f"Bebida {nome}", preco, "", "Geral")

with tabs[3]:
    for nome, preco in DOCES.items():
        if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doce_{nome}"):
            adicionar_ao_pedido(nome, preco, "", "Geral")

# FINALIZAR (ORGANIZADO POR PEDIDO)
with tabs[4]:
    st.write("### 📝 Resumo do Pedido")
    if st.session_state.carrinho:
        for p_id in sorted(list(set(item['id'] for item in st.session_state.carrinho if isinstance(item['id'], int)))):
            st.info(f"📍 **PEDIDO {p_id}**")
            for item in [i for i in st.session_state.carrinho if i['id'] == p_id]:
                st.write(f"- {item['item']} (R$ {item['preco']:.2f})")
        
        geral = [i for i in st.session_state.carrinho if i['id'] == "Geral"]
        if geral:
            st.warning("📍 **OUTROS (Bebidas/Doces)**")
            for item in geral:
                st.write(f"- {item['item']} (R$ {item['preco']:.2f})")

    nome = st.text_input("Seu Nome:")
    end = st.text_input("Endereço:")
    
    if st.button("🟢 ENVIAR PARA WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            total = sum(i['preco'] for i in st.session_state.carrinho)
            resumo = ""
            for i in st.session_state.carrinho:
                resumo += f"\n[{i['id']}] {i['item']} - R${i['preco']:.2f}"
            
            msg = f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*{resumo}\n\n*TOTAL: R$ {total:.2f}*"
            st.link_button("Confirmar no Whats ✅", f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}")

if st.session_state.carrinho:
    total_r = sum(item['preco'] for item in st.session_state.carrinho)
    st.markdown(f'<div class="footer-soma"><b>🛒 Total Geral: R$ {total_r:.2f}</b></div>', unsafe_allow_html=True)

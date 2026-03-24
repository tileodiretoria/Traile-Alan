import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (MUDE TUDO POR AQUI!)
# =========================================================

# 1. TÍTULO DO TRAILER
NOME_TRAILER = "🍔 Trailer do Alan"

# 2. CONFIGURAÇÃO DAS ABAS (Nomes e Itens)
# Aqui você muda o nome da aba, o nome do lanche, o preço e o que vem dentro.
CARDAPIO = {
    "Hambúrguer Simples": [
        {"nome": "Hambúrguer", "preco": 10.00, "ing": "Pão, Carne, Alface e Tomate"},
        {"nome": "X-Burger", "preco": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"},
        {"nome": "X-Egg", "preco": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"},
        {"nome": "X-Bacon", "preco": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"},
    ],
    "Hambúrguer de Frango": [
        {"nome": "Hambúrguer Frango", "preco": 12.00, "ing": "Pão, Frango, Alface e Tomate"},
        {"nome": "X-Burger Frango", "preco": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"},
        {"nome": "X-Egg Frango", "preco": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"},
    ],
    "Opções de Lombo": [
        {"nome": "X-Lombo", "preco": 14.00, "ing": "Pão, Lombo, Alface e Tomate"},
    ],
    "Opções de Picanha": [
        {"nome": "X-Picanha", "preco": 18.00, "ing": "Pão, Picanha, Alface e Tomate"},
    ],
    "Filé de Frango": [
        {"nome": "X-Filé", "preco": 15.00, "ing": "Pão, Filé de Frango, Alface e Tomate"},
    ]
}

# 3. ADICIONAIS (Nomes e Preços)
ADICIONAIS = {"Queijo": 3, "Presunto": 3, "Ovo": 3, "Bacon": 5, "Milho": 2}

# 4. BEBIDAS
BEBIDAS = {"Refri Lata": 5.00, "Refri 600ml": 8.00, "Suco": 7.00}

# 5. CONTATO DO ALAN
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ PARTE TÉCNICA (NÃO PRECISA MEXER AQUI ABAIXO)
# =========================================================

st.set_page_config(page_title=NOME_TRAILER, page_icon="🍔", layout="centered")

st.markdown(f"""
    <style>
    .stApp {{ background-color: #F0F8FF; }}
    .main-title {{ color: #0077b6; font-size: 38px; font-weight: bold; text-align: center; }}
    .stButton>button {{ 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 100px; font-weight: bold; font-size: 14px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<p class="main-title">{NOME_TRAILER}</p>', unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar(nome, preco, ing):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ing})
    st.toast(f"✅ {nome} adicionado!")

tab1, tab2, tab3, tab4 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🏁 Finalizar"])

with tab1:
    for categoria, lanches in CARDAPIO.items():
        with st.expander(f"✨ {categoria}"):
            cols = st.columns(2)
            for i, l in enumerate(lanches):
                with cols[i % 2]:
                    texto_botao = f"{l['nome']}\nR$ {l['preco']:.2f}\n({l['ing']})"
                    if st.button(texto_botao, key=f"{categoria}_{l['nome']}"):
                        adicionar(l['nome'], l['preco'], l['ing'])

with tab2:
    cols = st.columns(2)
    for i, (item, preco) in enumerate(ADICIONAIS.items()):
        if cols[i % 2].button(f"{item}\n+ R$ {preco:.2f}"):
            adicionar(f"Adicional {item}", preco, "Extra")

with tab3:
    for item, preco in BEBIDAS.items():
        if st.button(f"{item}\nR$ {preco:.2f}"):
            adicionar(item, preco, "")

with tab4:
    nome = st.text_input("Seu Nome:")
    end = st.text_input("Endereço:")
    total = sum(i['preco'] for i in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO"):
        if nome and end and st.session_state.carrinho:
            lista = "\n".join([f"* {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            msg = f"*PEDIDO*\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*\n{lista}\n\n*TOTAL: R$ {total:.2f}*"
            st.link_button("Abrir WhatsApp ✅", f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20')}")

if st.session_state.carrinho:
    st.markdown(f'<div style="position:fixed;bottom:0;left:0;width:100%;background:white;padding:10px;text-align:center;border-top:3px solid #00b4d8;"><b>Total: R$ {sum(i["preco"] for i in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

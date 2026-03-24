import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (AUTONOMIA TOTAL DO LEO)
# =========================================================

# 1. TÍTULOS DAS 5 ABAS
TITULO_ABA_1 = "Hambúrguer Simples"
TITULO_ABA_2 = "Hambúrguer de Frango"
TITULO_ABA_3 = "Hambúrguer de Lombo"
TITULO_ABA_4 = "Hambúrguer de Picanha"
TITULO_ABA_5 = "Filé de Frango"

# 2. CARDÁPIO DETALHADO (Mude nomes, preços e ingredientes aqui)
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

# 4. CONTATO WHATSAPP
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE (ESTRUTURA E CÁLCULOS)
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="centered")

# Estilo Visual (Cores e Rodapé Fixo)
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 110px; font-weight: bold; font-size: 14px; margin-bottom: 10px;
    }
    .footer-soma { 
        position: fixed; bottom: 0; left: 0; width: 100%; background: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
        font-size: 20px; color: #0077b6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

# Inicializa o carrinho vazio se for a primeira vez abrindo o site
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# Função simples para colocar itens na lista
def adicionar_ao_pedido(nome, preco, ingredientes):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ingredientes})
    st.toast(f"✅ Adicionado: {nome}")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# --- ABA DE LANCHES ---
with tabs[0]:
    for titulo, lanches in ITENS_CARDAPIO.items():
        with st.expander(f"✨ Opções de {titulo}"):
            c1, c2 = st.columns(2)
            for i, l in enumerate(lanches):
                coluna = c1 if i % 2 == 0 else c2
                # O botão mostra: Nome, Preço e Ingredientes
                if coluna.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                    adicionar_ao_pedido(l['n'], l['p'], l['ing'])

# --- ABA DE ADICIONAIS ---
with tabs[1]:
    c1, c2 = st.columns(2)
    for i, (nome, preco) in enumerate(ADICIONAIS.items()):
        coluna = c1 if i % 2 == 0 else c2
        if coluna.button(f"{nome}\n+ R$ {preco:.2f}"):
            adicionar_ao_pedido(f"Extra {nome}", preco, "Adicional")

# --- ABA DE BEBIDAS E DOCES ---
with tabs[2]:
    for nome, preco in BEBIDAS.items():
        if st.button(f"🥤 {nome} - R$ {preco:.2f}"):
            adicionar_ao_pedido(f"Refri {nome}", preco, "")

with tabs[3]:
    for nome, preco in DOCES.items():
        if st.button(f"🍰 {nome} - R$ {preco:.2f}"):
            adicionar_ao_pedido(nome, preco, "")

# --- ABA FINALIZAR ---
with tabs[4]:
    nome_usuario = st.text_input("Seu Nome:")
    end_usuario = st.text_input("Endereço Completo:")
    tel_usuario = st.text_input("Telefone:")
    obs_usuario = st.text_area("Observações do Pedido:")
    
    # --- EXPLICAÇÃO DA SOMA NO CÓDIGO ---
    # Pegamos o preço de cada item que está no carrinho e somamos todos
    valor_total = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 CONCLUIR E ENVIAR WHATSAPP"):
        if nome_usuario and end_usuario and st.session_state.carrinho:
            # Monta a lista de texto para o Zap
            txt_pedido = "\n".join([f"- {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            
            mensagem_final = (
                f"*PEDIDO - TRAILER DO ALAN*\n"
                f"*Cliente:* {nome_usuario}\n"
                f"*Endereço:* {end_usuario}\n"
                f"*Telefone:* {tel_usuario}\n\n"
                f"*ITENS:*\n{txt_pedido}\n\n"
                f"*OBS:* {obs_usuario}\n"
                f"*TOTAL: R$ {valor_total:.2f}*"
            )
            # Link que abre o WhatsApp
            link = f"https://wa.me/{WHATSAPP_ALAN}?text={mensagem_final.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Ir para o WhatsApp ✅", link)
        else:
            st.warning("Preencha seu nome, endereço e adicione itens ao carrinho!")

# --- BARRA DE SOMA AUTOMÁTICA (RODAPÉ) ---
# Se houver algo no carrinho, mostra o total lá embaixo
if st.session_state.carrinho:
    # Esta linha soma os preços de novo para mostrar na barra fixa
    total_rodape = sum(item['preco'] for item in st.session_state.carrinho)
    st.markdown(f'''
        <div class="footer-soma">
            <b>🛒 Valor Total do Pedido: R$ {total_rodape:.2f}</b>
        </div>
    ''', unsafe_allow_html=True)

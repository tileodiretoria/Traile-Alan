import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (AUTONOMIA TOTAL DO LEO)
# =========================================================

# 1. TÍTULOS DAS ABAS (Mude o texto entre aspas para mudar o nome da aba)
NOME_ABA_1 = "Hambúrguer Simples"
NOME_ABA_2 = "Hambúrguer de Frango"
NOME_ABA_3 = "Hambúrguer de Lombo"
NOME_ABA_4 = "Hambúrguer de Picanha"
NOME_ABA_5 = "Filé de Frango"

# 2. PREÇOS BASE (Altere o número para mudar o valor inicial de cada categoria)
PRECO_BASE_CARNE = 10.00
PRECO_BASE_FRANGO = 12.00
PRECO_BASE_LOMBO = 14.00
PRECO_BASE_PICANHA = 18.00
PRECO_BASE_FILE = 15.00

# 3. ADICIONAIS (Mude o nome ou o valor)
ADICIONAIS = {
    "Queijo": 3.00, "Presunto": 3.00, "Ovo": 3.00, 
    "Bacon": 5.00, "Milho": 2.00, "Batata": 4.00, "Catupiry": 5.00
}

# 4. BEBIDAS E DOCES
BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}
DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}

# 5. DADOS DO ALAN
WHATSAPP_ALAN = "5511999999999" # Coloque o número dele aqui (DDI + DDD + Número)

# =========================================================
# ⚙️ LÓGICA DO SISTEMA (NÃO PRECISA MEXER ABAIXO)
# =========================================================

st.set_page_config(page_title="Trailer do Alan", page_icon="🍔", layout="centered")

# Estilo Visual Azul
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #00b4d8; color: white; width: 100%; border-radius: 12px; 
        min-height: 110px; font-weight: bold; border: none; font-size: 14px; margin-bottom: 10px;
    }
    .footer-total { 
        position: fixed; bottom: 0; left: 0; width: 100%; background-color: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar(nome, preco, ing):
    st.session_state.carrinho.append({"item": nome, "preco": preco, "ing": ing})
    st.toast(f"✅ {nome} adicionado!")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

with tab1:
    # Lista com as 5 categorias e seus respectivos preços base e nomes das abas
    categorias = [
        {"nome": NOME_ABA_1, "tipo": "Carne", "pb": PRECO_BASE_CARNE},
        {"nome": NOME_ABA_2, "tipo": "Frango", "pb": PRECO_BASE_FRANGO},
        {"nome": NOME_ABA_3, "tipo": "Lombo", "pb": PRECO_BASE_LOMBO},
        {"nome": NOME_ABA_4, "tipo": "Picanha", "pb": PRECO_BASE_PICANHA},
        {"nome": NOME_ABA_5, "tipo": "Filé de Frango", "pb": PRECO_BASE_FILE},
    ]

    for cat in categorias:
        with st.expander(f"✨ Opções de {cat['nome']}"):
            tipo = cat['tipo']
            pb = cat['pb']
            col1, col2 = st.columns(2)
            
            # Aqui estão as 7 variações padrão que você pediu
            opcoes = [
                {"n": f"{tipo}", "p": pb, "ing": f"Pão, {tipo}, Alface e Tomate"},
                {"n": f"X-Burger {tipo}", "p": pb+5, "ing": f"Pão, {tipo}, Queijo, Alface e Tomate"},
                {"n": f"X-Egg {tipo}", "p": pb+8, "ing": f"Pão, {tipo}, Queijo, Ovo, Alface e Tomate"},
                {"n": f"X-Bacon {tipo}", "p": pb+10, "ing": f"Pão, {tipo}, Queijo, Bacon, Alface e Tomate"},
                {"n": f"X-Presunto {tipo}", "p": pb+7, "ing": f"Pão, {tipo}, Queijo, Presunto, Alface e Tomate"},
                {"n": f"X-Bacon Presunto {tipo}", "p": pb+13, "ing": f"Pão, {tipo}, Queijo, Bacon, Presunto, Alface e Tomate"},
                {"n": f"X-Egg Bacon Presunto {tipo}", "p": pb+16, "ing": f"Pão, {tipo}, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
            ]

            for i, l in enumerate(opcoes):
                col_target = col1 if i % 2 == 0 else col2
                btn_label = f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})"
                if col_target.button(btn_label, key=f"btn_{l['n']}_{cat['nome']}"):
                    adicionar(l['n'], l['p'], l['ing'])

with tab2:
    cols = st.columns(2)
    for i, (item, preco) in enumerate(ADICIONAIS.items()):
        if cols[i % 2].button(f"{item}\n+ R$ {preco:.2f}"):
            adicionar(f"Adicional {item}", preco, "Extra")

with tab3:
    for item, preco in BEBIDAS.items():
        if st.button(f"🥤 {item}\nR$ {preco:.2f}"):
            adicionar(item, preco, "")

with tab4:
    for item, preco in DOCES.items():
        if st.button(f"🍰 {item}\nR$ {preco:.2f}"):
            adicionar(item, preco, "")

with tab5:
    nome = st.text_input("Seu Nome:")
    end = st.text_input("Endereço Completo:")
    tel = st.text_input("Telefone de Contato:")
    comp = st.text_input("Complemento (Apto, Bloco, Referência):")
    obs = st.text_area("Observações (Ex: Sem cebola, ponto da carne):")

    total_final = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO PARA O WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            itens_lista = "\n".join([f"* {i['item']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
            mensagem = f"*PEDIDO - TRAILER DO ALAN*\n\n*Cliente:* {nome}\n*Endereço:* {end}\n*Complemento:* {comp}\n*Telefone:* {tel}\n\n*ITENS:*\n{itens_lista}\n\n*OBS:* {obs}\n\n*TOTAL: R$ {total_final:.2f}*"
            link_wa = f"https://wa.me/{WHATSAPP_ALAN}?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Confirmar e Abrir WhatsApp ✅", link_wa)
        else:
            st.error("Por favor, preencha o Nome, Endereço e escolha pelo menos um item!")

# Rodapé com a soma total sempre visível
if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total do Pedido: R$ {sum(item["preco"] for item in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

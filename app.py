import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Trailer do Alan - Cardápio", page_icon="🍔", layout="centered")

# --- ESTILO VISUAL (AZUL E BRANCO) ---
st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .main-title { color: #0077b6; font-size: 38px; font-weight: bold; text-align: center; margin-bottom: 5px; }
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
    # DEFINIÇÃO DAS CATEGORIAS
    # Para Carne, usamos apenas "Carne". Para Frango, "Hambúrguer de Frango" como você pediu.
    categorias = [
        {"nome": "Hambúrguer de Carne", "tipo": "Carne", "pb": 10},
        {"nome": "Hambúrguer de Frango", "tipo": "Hambúrguer de Frango", "pb": 12},
        {"nome": "Hambúrguer de Lombo", "tipo": "Lombo", "pb": 14},
        {"nome": "Hambúrguer de Picanha", "tipo": "Picanha", "pb": 18},
    ]

    for cat in categorias:
        with st.expander(f"✨ Opções de {cat['nome']}"):
            tipo = cat['tipo']
            pb = cat['pb']
            col1, col2 = st.columns(2)
            
            # Lista de lanches com descrições corrigidas
            lanches = [
                {"n": f"{tipo}", "p": pb, "ing": f"Pão, {tipo}, Alface e Tomate"},
                {"n": f"X-Burger {tipo}", "p": pb+5, "ing": f"Pão, {tipo}, Queijo, Alface e Tomate"},
                {"n": f"X-Egg {tipo}", "p": pb+8, "ing": f"Pão, {tipo}, Queijo, Ovo, Alface e Tomate"},
                {"n": f"X-Bacon {tipo}", "p": pb+10, "ing": f"Pão, {tipo}, Queijo, Bacon, Alface e Tomate"},
                {"n": f"X-Presunto {tipo}", "p": pb+7, "ing": f"Pão, {tipo}, Queijo, Presunto, Alface e Tomate"},
                {"n": f"X-Bacon Presunto {tipo}", "p": pb+13, "ing": f"Pão, {tipo}, Queijo, Bacon, Presunto, Alface e Tomate"},
                {"n": f"X-Egg Bacon Presunto {tipo}", "p": pb+16, "ing": f"Pão, {tipo}, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}
            ]

            for i, l in enumerate(lanches):
                col_target = col1 if i % 2 == 0 else col2
                btn_label = f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})"
                if col_target.button(btn_label, key=f"btn_{l['n']}_{cat['nome']}"):
                    adicionar(l['n'], l['p'], l['ing'])

    st.markdown("---")
    xtudo_ing = "Pão, Todos os bifes (Carne, Frango, Lombo e Picanha), Queijo, Ovo, Bacon, Presunto, Alface e Tomate"
    if st.button(f"👑 X-TUDO ESPECIAL ALAN\nR$ 45,00\n({xtudo_ing})"):
        adicionar("X-Tudo Especial Alan", 45.00, xtudo_ing)

# --- ADICIONAIS, BEBIDAS E FINALIZAÇÃO (IGUAL AO SEU ORIGINAL) ---
with tab2:
    adics = {"Queijo": 3, "Presunto": 3, "Ovo": 3, "Bacon": 5, "Milho": 2, "Batata": 4, "Catupiry": 5}
    cols = st.columns(2)
    for i, (item, preco) in enumerate(adics.items()):
        if cols[i % 2].button(f"{item}\n+ R$ {preco:.2f}"):
            adicionar(f"Adicional {item}", preco, "Extra")

with tab3:
    refris = {"Lata": 5, "600ml": 8, "1 Litro": 10, "2 Litros": 15}
    for tam, preco in refris.items():
        if st.button(f"🥤 Refri {tam}\nR$ {preco:.2f}"):
            adicionar(f"Refri {tam}", preco, "")

with tab4:
    doces = {"Brigadeiro": 4, "Beijinho": 4, "Doce Amendoim": 3, "Doce Morango": 5}
    for doce, preco in doces.items():
        if st.button(f"{doce}\nR$ {preco:.2f}"):
            adicionar(doce, preco, "")

with tab5:
    nome = st.text_input("Seu Nome:")
    tel = st.text_input("Telefone:")
    end = st.text_input("Endereço Completo:")
    obs = st.text_area("Observações (Ex: Sem cebola):")

    total_final = sum(item['preco'] for item in st.session_state.carrinho)
    
    if st.button("🟢 ENVIAR PEDIDO PELO WHATSAPP"):
        if nome and end and st.session_state.carrinho:
            itens_lista = "\n".join([f"* {i['item']} (Ingredientes: {i['ing']})" for i in st.session_state.carrinho])
            mensagem = f"*PEDIDO - TRAILER DO ALAN*\n\n*Cliente:* {nome}\n*Endereço:* {end}\n\n*ITENS:*\n{itens_lista}\n\n*OBS:* {obs}\n\n*TOTAL: R$ {total_final:.2f}*"
            # Substitua o número abaixo pelo do Alan
            link_wa = f"https://wa.me/5511999999999?text={mensagem.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Abrir WhatsApp ✅", link_wa)
        else:
            st.error("Preencha os dados e escolha um item!")

if st.session_state.carrinho:
    st.markdown(f'<div class="footer-total"><b>🛒 Total do Pedido: R$ {sum(item["preco"] for item in st.session_state.carrinho):.2f}</b></div>', unsafe_allow_html=True)

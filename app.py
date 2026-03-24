import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (BASE ORIGINAL DO LEO - NÃO MEXER)
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
        {"n": "X-Egg Picanha", "p": 26.00, "ing": "Persoalizado: Pão, Picanha, Queijo, Ovo, Alface e Tomate"},
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
        {"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer Simples, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}
    ]
}

ADICIONAIS_PAGOS = {"Bife Hambúrguer": 5.0, "Bife Frango": 5.0, "Bife Picanha": 8.0, "Bife Lombo": 6.0, "Filé Frango": 6.0, "Queijo": 3.0, "Presunto": 3.0, "Ovo": 3.0, "Bacon": 5.0, "Catupiry": 5.0}
CORTESIAS = {"Milho": 0.0, "Batata Palha": 0.0}
BEBIDAS = {"Lata": 5.0, "600ml": 8.0, "1 Litro": 10.0, "2 Litros": 15.0}
DOCES = {"Brigadeiro": 4.0, "Beijinho": 4.0, "Doce Amendoim": 3.0}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE (SUBSTITUIÇÃO E ORGANIZAÇÃO)
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

# Lógica de dicionário para manter cada "gaveta" separada
if 'pedidos' not in st.session_state:
    st.session_state.pedidos = {f"Lanche {i}": {"principal": None, "extras": []} for i in range(1, 7)}

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

LISTA_6 = [f"Lanche {i}" for i in range(1, 7)]

# ABA LANCHES
with tabs[0]:
    escolha = st.selectbox("📝 Selecione a vaga do pedido:", LISTA_6)
    for titulo, lanches in ITENS_CARDAPIO.items():
        with st.expander(f"✨ {titulo}"):
            c1, c2 = st.columns(2)
            for i, l in enumerate(lanches):
                coluna = c1 if i % 2 == 0 else c2
                if coluna.button(f"{l['n']}\nR$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                    # SUBSTITUIÇÃO: se clicar em outro, troca o lanche dessa vaga
                    st.session_state.pedidos[escolha]["principal"] = {"n": l['n'], "p": l['p']}
                    st.toast(f"✅ {escolha} definido!")

# ABA ADICIONAIS
with tabs[1]:
    escolha_add = st.selectbox("➕ Adicionar extras em:", LISTA_6, key="sel_add")
    st.write("### ➕ Extras (Cobrados)")
    c1, c2 = st.columns(2)
    for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
        coluna = c1 if i % 2 == 0 else c2
        if coluna.button(f"{nome}\n+ R$ {preco:.2f}", key=f"extra_pago_{i}"):
            st.session_state.pedidos[escolha_add]["extras"].append({"n": nome, "p": preco})
            st.toast(f"➕ Adicionado ao {escolha_add}")

# ABAS BEBIDAS E DOCES (Adicionando aos pedidos específicos)
with tabs[2]:
    escolha_beb = st.selectbox("🥤 Bebida para qual pedido?", LISTA_6, key="sel_beb")
    for nome, preco in BEBIDAS.items():
        if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"bebida_{nome}"):
            st.session_state.pedidos[escolha_beb]["extras"].append({"n": f"Bebida {nome}", "p": preco})
            st.toast(f"🥤 {nome} adicionada!")

with tabs[3]:
    escolha_doce = st.selectbox("🍰 Doce para qual pedido?", LISTA_6, key="sel_doce")
    for nome, preco in DOCES.items():
        if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doce_{nome}"):
            st.session_state.pedidos[escolha_doce]["extras"].append({"n": f"Doce {nome}", "p": preco})
            st.toast(f"🍰 {nome} adicionado!")

# ABA FINALIZAR
with tabs[4]:
    nome_u = st.text_input("Seu Nome:")
    end_u = st.text_input("Endereço:")
    
    total_geral = 0.0
    resumo_whats = ""
    
    st.write("### 🧾 Resumo do Pedido")
    for l_nome in LISTA_6:
        p = st.session_state.pedidos[l_nome]
        if p["principal"]:
            subtotal = p["principal"]["p"] + sum(e["p"] for e in p["extras"])
            total_geral += subtotal
            st.markdown(f"**📍 {l_nome}: {p['principal']['n']}**")
            for e in p["extras"]:
                st.write(f"- {e['n']} (R$ {e['p']:.2f})")
            st.write(f"**Subtotal: R$ {subtotal:.2f}**")
            st.write("---")
            resumo_whats += f"\n*{l_nome}: {p['principal']['n']}*\n" + "".join([f"- {e['n']}\n" for e in p['extras']]) + f"*Subtotal: R$ {subtotal:.2f}*\n"
    
    if st.button("🟢 CONCLUIR E ENVIAR WHATSAPP"):
        if nome_u and end_u and total_geral > 0:
            msg = f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome_u}\n*Endereço:* {end_u}\n{resumo_whats}\n*TOTAL GERAL: R$ {total_geral:.2f}*"
            link = f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}"
            st.link_button("Ir para o WhatsApp ✅", link)

if total_geral > 0:
    st.markdown(f'<div class="footer-soma"><b>🛒 Valor Total: R$ {total_geral:.2f}</b></div>', unsafe_allow_html=True)

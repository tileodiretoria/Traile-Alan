import streamlit as st

# =========================================================
# 🛠️ PAINEL DE CONTROLE (BASE ORIGINAL DO LEO - INTEGRAL)
# =========================================================

TITULO_ABA_1 = "Hambúrguer Simples"
TITULO_ABA_2 = "Hambúrguer de Frango"
TITULO_ABA_3 = "Hambúrguer de Lombo"
TITULO_ABA_4 = "Hambúrguer de Picanha"
TITULO_ABA_5 = "Filé de Frango"
TITULO_ABA_6 = "🔥 X-TUDO"

ITENS_CARDAPIO = {
    TITULO_ABA_1: [{"n": "Hambúrguer", "p": 10.00, "ing": "Pão, Carne, Alface e Tomate"}, {"n": "X-Burger", "p": 15.00, "ing": "Pão, Carne, Queijo, Alface e Tomate"}, {"n": "X-Egg", "p": 18.00, "ing": "Pão, Carne, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon", "p": 20.00, "ing": "Pão, Carne, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto", "p": 17.00, "ing": "Pão, Carne, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto", "p": 23.00, "ing": "Pão, Carne, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto", "p": 26.00, "ing": "Pão, Carne, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_2: [{"n": "Hambúrguer Frango", "p": 12.00, "ing": "Pão, Frango, Alface e Tomate"}, {"n": "X-Burger Frango", "p": 17.00, "ing": "Pão, Frango, Queijo, Alface e Tomate"}, {"n": "X-Egg Frango", "p": 20.00, "ing": "Pão, Frango, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Frango", "p": 22.00, "ing": "Pão, Frango, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Frango", "p": 19.00, "ing": "Pão, Frango, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Frango", "p": 25.00, "ing": "Pão, Frango, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Frango", "p": 28.00, "ing": "Pão, Frango, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_3: [{"n": "Hambúrguer Lombo", "p": 14.00, "ing": "Pão, Lombo, Alface e Tomate"}, {"n": "X-Burger Lombo", "p": 19.00, "ing": "Pão, Lombo, Queijo, Alface e Tomate"}, {"n": "X-Egg Lombo", "p": 22.00, "ing": "Pão, Lombo, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Lombo", "p": 24.00, "ing": "Pão, Lombo, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Lombo", "p": 21.00, "ing": "Pão, Lombo, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Lombo", "p": 27.00, "ing": "Pão, Lombo, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Lombo", "p": 30.00, "ing": "Pão, Lombo, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_4: [{"n": "Hambúrguer Picanha", "p": 18.00, "ing": "Pão, Picanha, Alface e Tomate"}, {"n": "X-Burger Picanha", "p": 23.00, "ing": "Pão, Picanha, Queijo, Alface e Tomate"}, {"n": "X-Egg Picanha", "p": 26.00, "ing": "Pão, Picanha, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Picanha", "p": 28.00, "ing": "Pão, Picanha, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Picanha", "p": 25.00, "ing": "Pão, Picanha, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Picanha", "p": 31.00, "ing": "Pão, Picanha, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Picanha", "p": 34.00, "ing": "Pão, Picanha, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_5: [{"n": "Filé de Frango", "p": 15.00, "ing": "Pão, Filé, Alface e Tomate"}, {"n": "X-Burger Filé", "p": 20.00, "ing": "Pão, Filé, Queijo, Alface e Tomate"}, {"n": "X-Egg Filé", "p": 23.00, "ing": "Pão, Filé, Queijo, Ovo, Alface e Tomate"}, {"n": "X-Bacon Filé", "p": 25.00, "ing": "Pão, Filé, Queijo, Bacon, Alface e Tomate"}, {"n": "X-Presunto Filé", "p": 22.00, "ing": "Pão, Filé, Queijo, Presunto, Alface e Tomate"}, {"n": "X-Bacon Presunto Filé", "p": 28.00, "ing": "Pão, Filé, Queijo, Bacon, Presunto, Alface e Tomate"}, {"n": "X-Egg Bacon Presunto Filé", "p": 31.00, "ing": "Pão, Filé, Queijo, Ovo, Bacon, Presunto, Alface e Tomate"}],
    TITULO_ABA_6: [{"n": "X-TUDO DO ALAN", "p": 45.00, "ing": "Picanha, Lombo, Filé Frango, Hambúrguer, Queijo, Presunto, Ovo, Bacon, Alface, Tomate, Milho e Batata"}]
}

ADICIONAIS_PAGOS = {"Bife de Hambúrguer": 5.00, "Bife de Frango": 5.00, "Bife de Picanha": 8.00, "Bife de Lombo": 6.00, "Filé de Frango": 6.00, "Queijo": 3.00, "Presunto": 3.00, "Ovo": 3.00, "Bacon": 5.00, "Catupiry": 5.00}
BEBIDAS = {"Lata": 5.00, "600ml": 8.00, "1 Litro": 10.00, "2 Litros": 15.00}
DOCES = {"Brigadeiro": 4.00, "Beijinho": 4.00, "Doce Amendoim": 3.00}
WHATSAPP_ALAN = "5511999999999"

# =========================================================
# ⚙️ MOTOR DO SITE
# =========================================================

st.set_page_config(page_title="Trailer do Alan", layout="wide") # Mudei para wide para caber a coluna lateral

st.markdown("""
    <style>
    .stApp { background-color: #F0F8FF; }
    .stButton>button { 
        background-color: #0077b6; color: white; border-radius: 12px; 
        min-height: 80px; font-weight: bold; font-size: 14px; margin-bottom: 5px;
    }
    .panel-visual { background: white; padding: 20px; border-radius: 15px; border: 2px solid #0077b6; position: sticky; top: 20px; }
    .lanche-card { background: #e3f2fd; padding: 10px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #0077b6; }
    .footer-soma { position: fixed; bottom: 0; left: 0; width: 100%; background: white; padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100; font-size: 20px; color: #0077b6; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'lanches_fechados' not in st.session_state: st.session_state.lanches_fechados = []
if 'lanche_atual' not in st.session_state: st.session_state.lanche_atual = {"n": None, "p": 0.0, "ing": "", "extras": []}
if 'id_atual' not in st.session_state: st.session_state.id_atual = 1

# DIVISÃO DA TELA EM DUAS COLUNAS
col_menu, col_visual = st.columns([0.65, 0.35])

with col_menu:
    tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

    if st.session_state.id_atual <= 6:
        with tabs[0]: # ABA LANCHES (IDÊNTICA À FOTO)
            st.info(f"📍 Montando: Lanche {st.session_state.id_atual}")
            for titulo, lanches in ITENS_CARDAPIO.items():
                with st.expander(f"✨ {titulo}"):
                    for i, l in enumerate(lanches):
                        if st.button(f"{l['n']} - R$ {l['p']:.2f}\n({l['ing']})", key=f"btn_{titulo}_{i}"):
                            st.session_state.lanche_atual["n"] = l['n']
                            st.session_state.lanche_atual["p"] = l['p']
                            st.session_state.lanche_atual["ing"] = l['ing']
                            st.rerun()

        with tabs[1]: # ABA ADICIONAIS
            for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
                if st.button(f"{nome} (+R$ {preco:.2f})", key=f"extra_{i}"):
                    st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                    st.rerun()

        with tabs[2]: # ABA BEBIDAS
            for nome, preco in BEBIDAS.items():
                if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"beb_{nome}"):
                    st.session_state.lanche_atual["extras"].append({"n": f"Bebida {nome}", "p": preco})
                    st.rerun()

        with tabs[3]: # ABA DOCES
            for nome, preco in DOCES.items():
                if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doc_{nome}"):
                    st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                    st.rerun()

    with tabs[4]: # ABA FINALIZAR
        nome_u = st.text_input("Seu Nome:")
        end_u = st.text_input("Endereço:")
        if st.button("🟢 CONCLUIR PEDIDO E ENVIAR WHATSAPP", type="primary"):
            # Lógica de envio final...
            pass

# COLUNA DA DIREITA: VISUALIZAÇÃO DOS LANCHES 1 AO 6
with col_visual:
    st.markdown('<div class="panel-visual">', unsafe_allow_html=True)
    st.subheader("📋 Resumo da Montagem")
    
    # 1. Mostrar lanches que já foram travados (Lanche 1, 2...)
    for idx, l in enumerate(st.session_state.lanches_fechados):
        st.markdown(f"""<div class="lanche-card" style="background: #cfd8dc; border-left-color: #546e7a;">
        <b>✅ Lanche {idx+1}: {l['n']}</b><br><small>{l['ing']}</small></div>""", unsafe_allow_html=True)

    # 2. Mostrar o lanche que está sendo montado AGORA
    if st.session_state.id_atual <= 6:
        st.markdown(f"### 🍔 Lanche {st.session_state.id_atual}")
        if st.session_state.lanche_atual["n"]:
            st.success(f"**{st.session_state.lanche_atual['n']}**")
            st.caption(f"Ingredientes: {st.session_state.lanche_atual['ing']}")
            for i, e in enumerate(st.session_state.lanche_atual["extras"]):
                c1, c2 = st.columns([0.8, 0.2])
                c1.write(f"• {e['n']}")
                if c2.button("🗑️", key=f"del_{i}"):
                    st.session_state.lanche_atual["extras"].pop(i)
                    st.rerun()
            
            # BOTÃO DE TRAVA: SÓ PASSA PRO PRÓXIMO SE CLICAR AQUI
            if st.button(f"🔒 FINALIZAR LANCHE {st.session_state.id_atual}", use_container_width=True):
                st.session_state.lanches_fechados.append(st.session_state.lanche_atual.copy())
                st.session_state.lanche_atual = {"n": None, "p": 0.0, "ing": "", "extras": []}
                st.session_state.id_atual += 1
                st.rerun()
        else:
            st.warning("Selecione um lanche na aba ao lado.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# RODAPÉ COM TOTAL GERAL
total_g = sum([l['p'] + sum(e['p'] for e in l['extras']) for l in st.session_state.lanches_fechados])
if st.session_state.lanche_atual['n']:
    total_g += st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras'])
st.markdown(f'<div class="footer-soma"><b>TOTAL DO PEDIDO: R$ {total_g:.2f}</b></div>', unsafe_allow_html=True)

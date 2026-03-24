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
        display: flex; align-items: center; justify-content: center;
    }
    .footer-soma { 
        position: fixed; bottom: 0; left: 0; width: 100%; background: white; 
        padding: 15px; text-align: center; border-top: 3px solid #00b4d8; z-index: 100;
        font-size: 20px; color: #0077b6;
    }
    .resumo-lateral { background: #fff3e0; padding: 10px; border-radius: 8px; border: 1px solid #ff9800; margin-bottom: 15px; }
    .btn-excluir { background-color: #ff5252 !important; min-height: 30px !important; height: 30px !important; width: 30px !important; padding: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 style="text-align:center; color:#0077b6;">🍔 Trailer do Alan</h1>', unsafe_allow_html=True)

if 'lanches_fechados' not in st.session_state: st.session_state.lanches_fechados = []
if 'lanche_atual' not in st.session_state: st.session_state.lanche_atual = {"n": None, "p": 0.0, "extras": []}
if 'id_atual' not in st.session_state: st.session_state.id_atual = 1

def mostrar_resumo_atual():
    """Função para mostrar o que está sendo montado em cada aba com opção de excluir"""
    if st.session_state.lanche_atual["n"] or st.session_state.lanche_atual["extras"]:
        with st.container():
            st.markdown(f'<div class="resumo-lateral"><b>🧐 Vendo Lanche {st.session_state.id_atual}:</b></div>', unsafe_allow_html=True)
            if st.session_state.lanche_atual["n"]:
                st.write(f"🍔 **{st.session_state.lanche_atual['n']}** (R$ {st.session_state.lanche_atual['p']:.2f})")
            
            # Lista de extras com botão de excluir individual
            for i, extra in enumerate(st.session_state.lanche_atual["extras"]):
                col_texto, col_btn = st.columns([0.8, 0.2])
                col_texto.write(f"  • {extra['n']} (R$ {extra['p']:.2f})")
                if col_btn.button("🗑️", key=f"del_{st.session_state.id_atual}_{i}"):
                    st.session_state.lanche_atual["extras"].pop(i)
                    st.rerun()
            st.write("---")

tabs = st.tabs(["🍔 Lanches", "➕ Adicionais", "🥤 Bebidas", "🍰 Doces", "🏁 Finalizar"])

# MONTAGEM
if st.session_state.id_atual <= 6:
    # ABA LANCHES
    with tabs[0]:
        mostrar_resumo_atual()
        st.info(f"📍 Selecione o Lanche {st.session_state.id_atual}")
        for titulo, lanches in ITENS_CARDAPIO.items():
            with st.expander(f"✨ {titulo}"):
                c1, c2 = st.columns(2)
                for i, l in enumerate(lanches):
                    coluna = c1 if i % 2 == 0 else c2
                    if coluna.button(f"{l['n']}\nR$ {l['p']:.2f}", key=f"btn_{titulo}_{i}"):
                        st.session_state.lanche_atual["n"] = l['n']
                        st.session_state.lanche_atual["p"] = l['p']
                        st.rerun()

    # ABA ADICIONAIS
    with tabs[1]:
        mostrar_resumo_atual()
        st.write("### ➕ Adicionar Extras")
        c1, c2 = st.columns(2)
        for i, (nome, preco) in enumerate(ADICIONAIS_PAGOS.items()):
            coluna = c1 if i % 2 == 0 else c2
            if coluna.button(f"{nome}\n+ R$ {preco:.2f}", key=f"extra_{i}"):
                st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                st.rerun()

    # ABAS BEBIDAS E DOCES
    with tabs[2]:
        mostrar_resumo_atual()
        for nome, preco in BEBIDAS.items():
            if st.button(f"🥤 {nome} - R$ {preco:.2f}", key=f"beb_{nome}"):
                st.session_state.lanche_atual["extras"].append({"n": f"Bebida {nome}", "p": preco})
                st.rerun()

    with tabs[3]:
        mostrar_resumo_atual()
        for nome, preco in DOCES.items():
            if st.button(f"🍰 {nome} - R$ {preco:.2f}", key=f"doc_{nome}"):
                st.session_state.lanche_atual["extras"].append({"n": nome, "p": preco})
                st.rerun()

# ABA FINALIZAR
with tabs[4]:
    nome_u = st.text_input("Seu Nome:")
    end_u = st.text_input("Endereço:")
    tel_u = st.text_input("Telefone:")
    
    st.markdown("### 🧾 Resumo Final")
    total_ped = 0.0
    resumo_whats = ""

    # Lanches que já foram fechados (Estilo da sua foto!)
    for idx, l in enumerate(st.session_state.lanches_fechados):
        sub = l['p'] + sum(e['p'] for e in l['extras'])
        total_ped += sub
        st.markdown(f'<div style="background:#e3f2fd; padding:10px; border-radius:8px; margin-bottom:5px;">✅ <b>LANCHE {idx+1}: {l["n"]}</b> (R$ {sub:.2f})</div>', unsafe_allow_html=True)
        resumo_whats += f"\n*LANCHE {idx+1}: {l['n']}*\n" + "".join([f"- {e['n']}\n" for e in l['extras']]) + f"*Subtotal: R$ {sub:.2f}*\n"

    # Lanche em montagem
    if st.session_state.lanche_atual["n"]:
        sub_atual = st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras'])
        st.markdown(f'<div style="background:#fff3e0; padding:10px; border-radius:8px;">⏳ <b>LANCHE {st.session_state.id_atual}: {st.session_state.lanche_atual["n"]}</b> (R$ {sub_atual:.2f})</div>', unsafe_allow_html=True)
        
        if st.button(f"🔒 FECHAR LANCHE {st.session_state.id_atual} E MONTAR OUTRO"):
            st.session_state.lanches_fechados.append(st.session_state.lanche_atual.copy())
            st.session_state.lanche_atual = {"n": None, "p": 0.0, "extras": []}
            st.session_state.id_atual += 1
            st.rerun()

    if st.button("🟢 ENVIAR PEDIDO COMPLETO", type="primary"):
        total_final = total_ped + (st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras']))
        if nome_u and end_u and total_final > 0:
            # Lógica para incluir o lanche atual se não tiver sido fechado
            msg = f"*PEDIDO TRAILER DO ALAN*\n*Cliente:* {nome_u}\n*Endereço:* {end_u}\n\n*ITENS:*{resumo_whats}\n*TOTAL: R$ {total_final:.2f}*"
            st.link_button("Ir para WhatsApp ✅", f"https://wa.me/{WHATSAPP_ALAN}?text={msg.replace(' ', '%20').replace('\n', '%0A')}")

# RODAPÉ
rodape_val = total_ped + st.session_state.lanche_atual['p'] + sum(e['p'] for e in st.session_state.lanche_atual['extras'])
if rodape_val > 0:
    st.markdown(f'<div class="footer-soma"><b>🛒 TOTAL: R$ {rodape_val:.2f}</b></div>', unsafe_allow_html=True)
